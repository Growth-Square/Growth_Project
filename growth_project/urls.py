from django.conf.urls import patterns, include, url
from django.contrib import admin
from growth_project.apps.main import views as viewsGrowth

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('growth_project.apps.main.urls', namespace="main")),
                       url(r'', include('growth_project.apps.users.urls', namespace="users")),

                       # Social auth urls
                       url(r'', include('social.apps.django_app.urls', namespace="social")),
                       url(r'', include('django.contrib.auth.urls', namespace="auth")),

                       # User auth urls
                       url(r'^accounts/login/$', 'growth_project.views.login'),
                       url(r'^accounts/auth/$', 'growth_project.views.auth_view'),
                       url(r'^accounts/logout/$', 'growth_project.views.logout'),
                       url(r'^accounts/loggedin/$', 'growth_project.views.loggedin'),
                       url(r'^accounts/invalid_login/$', 'growth_project.views.invalid_login'),
                       url(r'^accounts/new/$', 'growth_project.views.new'),

                       # Main functions
                       url(r'^dashboard/$', viewsGrowth.dashboard, name='dashboard'),
                       url(r'^dashboard/selector/$', viewsGrowth.selector, name='selector'),
                       # url(r'^dashboard/designer/$', viewsGrowth.designer, name='designer'),
                       # url(r'^dashboard/designer/(\d{4})/$', viewsGrowth.designer, name='designer'),
                       url(r'^designer/(?P<template_name>\w+)/$', viewsGrowth.designer, name='designer'),
                       # (?P<name>\w+)/

                       # Reset password urls
                       url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset',
                           name='reset_password_reset1'),
                       url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
                           name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
                       url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),


                       # Admin urls
                       url(r'^admin/', include(admin.site.urls)),

)
# ADMIN> gborde 154060gb - 123456
