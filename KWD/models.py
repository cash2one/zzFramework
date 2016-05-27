# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class User(models.Model):
    u"""用户表，登录时用username字段，email字段用于发送邮件"""
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    u"""项目表"""
    project = models.CharField(max_length=150)
    creator = models.ForeignKey(User)
    createtime = models.DateTimeField()
    memo = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.project


class Suite(models.Model):
    u"""套件表，所有的case均需组织在套件中执行，才能生成报告、发送邮件"""
    suite = models.CharField(max_length=150)
    project = models.ForeignKey(Project)
    creator = models.ForeignKey(User)
    memo = models.TextField(max_length=500, blank=True)
    createtime = models.DateTimeField()
    modifytime = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.suite


class Case(models.Model):
    u"""用例表，可以单独执行，作为测试用例是否可用；想要生成报告、发送邮件，需要组织到suite中"""
    case = models.CharField(max_length=150)
    suite = models.ForeignKey(Suite, blank=True)
    type = models.CharField(max_length=10, blank=True, choices=(('API', u'接口测试用例'), ('UI', u'UI测试用例'),))
    creator = models.ForeignKey(User)
    memo = models.TextField(max_length=500, blank=True)
    file = models.FileField(upload_to='./upload/', blank=True)
    createtime = models.DateTimeField()
    modifytime = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.case


class Action(models.Model):
    u"""操作表，存放所有支持的UI操作，UI步骤中只能选择操作表中的action"""
    action = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.action


class Browser(models.Model):
    u"""浏览器表，存放所有支持的浏览器类型"""
    browser = models.CharField(max_length=20, unique=True)
    profile = models.FileField(upload_to='./upload/', blank=True)

    def __unicode__(self):
        return self.browser


class Step(models.Model):
    u"""步骤表，存放UI操作步骤，用以组织成UI测试的case，其中action仅能选择Action表中项，browser仅支持Browser表中的浏览器"""
    step = models.CharField(max_length=150)
    case = models.ForeignKey(Case)
    action = models.ForeignKey(Action)
    browser = models.ForeignKey(Browser, blank=True)
    url = models.CharField(max_length=500, blank=True)
    by = models.CharField(max_length=20, blank=True)
    value = models.TextField(blank=True)
    sleep = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey(User)
    memo = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return self.step


class History(models.Model):
    u"""历史表，记录所有操作历史，包括增删改project、suite、case、step等"""
    time = models.DateTimeField()
    user = models.ForeignKey(User)
    model = models.CharField(max_length=200, choices=(('1', 'Project'), ('2', 'Suite'), ('3', 'Case'), ('4', 'Step'),))
    operate = models.CharField(max_length=200, choices=(('1', 'Create'), ('2', 'Modify'), ('3', 'Delete'),))
    be_operated = models.CharField(max_length=150)


# class SuiteAdmin(admin.ModelAdmin):
#     list_display = ('name', 'createtime', 'modifytime')
#
#
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'suite', 'createtime', 'modifytime')
#
#
# class StepAdmin(admin.ModelAdmin):
#     list_display = ('step', 'action', 'browser', 'url', 'by', 'value', 'sleep')
#
# admin.site.register(Suite, SuiteAdmin)
# admin.site.register(Case, CaseAdmin)
# admin.site.register(Step, StepAdmin)
