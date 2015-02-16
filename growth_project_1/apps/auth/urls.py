# Import the utility functions from the URL handling library
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        # Map the root URL / to the 'app.hello.reset' view that wraps
        # the built-in password reset view. The first argument is a
        # regular expression that matches the path of the URL after /. Since
        # '^$' matches an empty string, this pattern matches the root URL /.
        url(r'^$', 'app.hello.reset', name='reset'),
        
        # Map the 'app.hello.reset_confirm' view that wraps around built-in password
        # reset confirmation view, to the password reset confirmation links.
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'app.hello.reset_confirm', name='password_reset_confirm'),
        
        # Map the 'app.hello.success' view to the success message page.
        url(r'^success/$', 'app.hello.success', name='success'),
)
        
