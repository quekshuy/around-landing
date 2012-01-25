
from django.conf.urls.defaults import patterns, url

from django.views.generic import TemplateView
from views import SubmitArdLeadView

urlpatterns = patterns('',

            # First landing on signup form
            url(r'^$', SubmitArdLeadView.as_view(), 
                {'step_number': 0}, 
                name='merchant-signup-0'),

            # Sign up Form (in the middle)
            url(r'(?P<step_number>\d{1})/$', SubmitArdLeadView.as_view(),
                name='merchant-signup-middle'),

            # Successful Sign Up
            url(r'^success/$', TemplateView.as_view(
                    template_name='pages/merchant_signup_success.html'), 
                name='merchant-signup-success'),

            # Error at signup
            url(r'^error/$', TemplateView.as_view(
                    template_name='pages/merchant_signup_error.html'),
                name='merchant-signup-error'),
        )
