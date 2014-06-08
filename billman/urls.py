from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'billman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'account.views.login'),

    # account (register, login, password):
    url(r'^accounts/login/$', 'account.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^accounts/password/change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^accounts/password/change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^accounts/register/$', 'account.views.register', name='register'),
    url(r'^accounts/register/done/$', 'account.views.register_done', name='register_done'),

    url(r'^bill/fetch/$', 'bill.views.fetch', name='bill_fetch'),
    url(r'^bill/(\d+)/addTransaction/$', 'bill.views.addTransaction', name='bill_add'),
)
