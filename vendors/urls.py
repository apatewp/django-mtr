from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'vendors.views.vendors_index'),
    #url(r'^new_part/$', 'parts.views.new_part'),
    #url(r'^edit/(?P<part_number>.+)/$', 'parts.views.edit_part'),    
    url(r'^(?P<vendor_id>\d+)/$', 'vendors.views.vendor'),
    url(r'^po/(?P<purchase_order>.+)/$', 'vendors.views.purchase_order'),
    
)
