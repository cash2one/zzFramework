# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from KWD.models import *


def index(request, user=None):
    suites = Suite.objects.all()
    cases = Case.objects.all()
    steps = Step.objects.all()

    with open('D:\\Keyworddriven\\KWD\\framework\\testapi\\suite\\test_suite.py') as f:
        fun_num = 0
        for line in f:
            if 'def ' in line:
                fun_num += 1
    from KWD.framework.testapi.suite import test_suite
    suite_func = None
    for pro, value in vars(test_suite).iteritems():
        if '__' not in pro and pro != 'unittest':
            suite_func = pro

    import os
    for root, dirs, files in os.walk('D:\\Keyworddriven\\KWD\\framework\\testapi\\case'):
        for fi in files:
            if fi[-3:] != '.py':
                files.remove(fi)
        files.remove('__init__.py')

    t = loader.get_template('index.html')
    c = Context({'suites': suites, 'cases': cases, 'steps': steps, 'fun_num': fun_num, 'files': files, 'file_num': len(files), 'pro': suite_func, 'user': user})
    return HttpResponse(t.render(c))


def run(request):
    from KWD.framework.testapi.suite.test_suite import suite
    from KWD.framework.tools.HTMLTestRunner import HTMLTestRunner
    filename = 'D:\\Keyworddriven\\KWD\\templates\\report.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'直购2.0 接口测试报告', description=u'测试用例执行情况见下表：')
    runner.run(suite())
    fp.close()
    return render(request, 'report.html')


def view(request):
    return render(request, 'report.html')


def base(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    from models import User
    u = User.objects.get(username=username)
    if u.password == password:
        return index(request, u)
    else:
        return base(request)


def addcase(request):
    return render(request, 'addcase.html')


def project_list(request):
    from models import Project
    projects = Project.objects.all()
    c = Context({'projects': projects})
    return render(request, 'project.html', context=c)
