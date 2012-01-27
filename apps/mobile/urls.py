
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
            # landing page
            url('^$', TemplateView.as_view(template_name='mobile/start_page.html'),
            name='mobile-start'),
        )

