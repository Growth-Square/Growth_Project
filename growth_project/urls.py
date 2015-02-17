from django.conf.urls import patterns, include, url
from django.contrib import admin
from growth_project.apps.growth import views as viewsGrowth

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('growth_project.apps.growth.urls', namespace="growth")),
                       url(r'', include('growth_project.apps.users.urls', namespace="users")),

                       # User auth urls
                       url(r'^accounts/login/$', 'growth_project.views.login'),
                       url(r'^accounts/auth/$', 'growth_project.views.auth_view'),
                       url(r'^accounts/logout/$', 'growth_project.views.logout'),
                       url(r'^accounts/loggedin/$', 'growth_project.views.loggedin'),
                       url(r'^accounts/invalid_login/$', 'growth_project.views.invalid_login'),
                       url(r'^accounts/new/$', 'growth_project.views.new'),

                       url(r'^dashboard/$', viewsGrowth.dashboard),


                       # Python social auth urls
                       url(r'', include('social.apps.django_app.urls', namespace="social")),
                       url(r'', include('django.contrib.auth.urls', namespace="auth")),
                       #url(r'', include('social_auth.urls')),

                       # Admin urls
                       url(r'^admin/', include(admin.site.urls)),

)
# ADMIN> gborde 154060gb - 123456
