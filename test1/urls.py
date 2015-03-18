from django.conf.urls import *
from test1.view import hello,current_datetime,hour_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^hello/$', hello),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d+)/$',hour_ahead),
)
