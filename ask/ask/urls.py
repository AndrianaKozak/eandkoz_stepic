from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/','login', name='login'),
    url(r'^signup/', 'signup', name='signup'),
    url(r'^question/(\d+)/', 'question', name='question'),
    url(r'^ask/', 'ask', name='ask'),
    url(r'^popular/', 'popular', name='popular'),
    url(r'^new/', 'new', name='new'),
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^ask/', include('ask.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

