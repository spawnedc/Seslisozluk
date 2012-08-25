from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<word>\w+)/$', 'sesli_sozluk.views.parse_response', name='home'),
)
