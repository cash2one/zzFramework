from django.conf.urls import include, url
from django.contrib import admin
from KWD.views import index, run, view, base, login, addcase, project_list

urlpatterns = [
    # Examples:
    # url(r'^$', 'Keyworddriven.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base),
    url(r'^login', login),
    url(r'^index', index),

    url(r'^run', run),
    url(r'^view', view),
    url(r'^addcase', addcase),
    url(r'^project', project_list),
]
