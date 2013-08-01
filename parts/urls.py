from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'parts.views.parts_index'),
    url(r'^new_part/$', 'parts.views.new_part'),
    url(r'^edit/(?P<part_number>\w+)/$', 'parts.views.edit_part'),    
    url(r'^(?P<part_number>\w+)/$', 'parts.views.part'),
    
)
