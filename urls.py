
from django.conf.urls.defaults import patterns, url, include
from django.views.generic import TemplateView
from django.contrib import admin

from pages.views import (
        ContactUsPage, 
        MerchantsPage,
        HowItWorksPage,
        RequestMerchantPage
        )

admin.autodiscover()

urlpatterns = patterns('',

    # Landing page
    (r'^$', TemplateView.as_view(template_name='pages/start_page.html')),

    # About
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'),
        name='page-about'),

    # How It Works
    url(r'^how-it-works/$', HowItWorksPage.as_view(), name='page-how'),

    # Contact Us
    url(r'^contact/$', ContactUsPage.as_view(), name='page-contact-us'),

    # Support
    url(r'support/$', TemplateView.as_view(template_name='pages/support.html'),
        name='page-support'),

    # Merchants
    url(r'^merchants/$', MerchantsPage.as_view(), name='page-merchants'),

    # Request for merchants to come on around
    url(r'^mrequest/$', RequestMerchantPage.as_view(), 
        name='page-merchant-request'),
    # Request for merchants to come on around (SUCCESS)
    url(r'^mrequest/success/$', 
        TemplateView.as_view(template_name='pages/merchant_request_success.html'),
        name='page-request-success'),
    # For lead generation
    (r'^merchant/signup/', include('leads.urls')),

    # For mobile
    url(r'^mobile/$', include('mobile.urls')),

    # For lead generation
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
   #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   (r'^admin/', include(admin.site.urls)),

)

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

