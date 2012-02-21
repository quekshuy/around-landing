
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from django.views.generic.base import TemplateResponseMixin
from django.core.urlresolvers import reverse

from leads.forms import ArdLeadForm, ArdMerchantRequestForm
from leads.utils import default_mailer
from models import ArdMerchant

#-------------------------------------------------------------------------------- 

class HowItWorksPage(TemplateView):
    template_name = 'pages/how_it_works.html'
    def get_context_data(self, **kwargs):
        return { 'page_how' : 1 }

#-------------------------------------------------------------------------------- 

class RequestMerchantPage(TemplateResponseMixin, View):
    template_name = 'pages/request.html'
    success_email = """
                        Hey hey, someone likes around!. They would like to 
                        see a particular merchant onboard with us.
                        Here are the details: 

                        Name: %s
                        Email: %s
                        Contact: %s
                        Brand Requested: %s
                        Specific Outlet Address: %s

                    """

    def post(self, request):
        form = ArdMerchantRequestForm(request.POST)
        if form.is_valid():
            m = form.save()
            cd = form.cleaned_data
            default_mailer.post_message(
                        "contact@around.com.sg",
                        settings.SALES_TEAM_EMAILS,
                        "Someone would like a merchant on around!",
                        self.success_email % (
                            cd['name'],
                            cd['email'],
                            cd['contact_number'],
                            cd['brand_name'],
                            cd['outlet_address'])
                        )
            return redirect(reverse('page-request-success'))
        context = dict(form=form)
        return render(request, self.template_name, context)


    def get(self, request):
        form = ArdMerchantRequestForm()
        context = dict(form=form)
        return render(request, self.template_name, context)

#-------------------------------------------------------------------------------- 

class ContactUsPage(TemplateResponseMixin, View):
    template_name = 'pages/contact_us.html'

    def success(self, m):
        '''
            Does the necessary actions for a successful submission
            for contact.
        '''
        msg = """
                Someone has requested to be our merchant. Details as 
                follows:

                Name: %s
                Contact: %s
                Email: %s
                Company Name: %s

                Let's make his/her day. :)

                HO SAY AH!

              """ % ( m.name, m.contact_number, m.email, m.brand_name)
        r = default_mailer.post_message(
                "contact@around.com.sg",
                settings.SALES_TEAM_EMAILS,
                'Interested Merchant Alert',
                msg
                )
        if r.status_code >= 300:
            raise Exception('Merchant alert but no email sent!')
        

    def post(self, request):
        form = ArdLeadForm(request.POST)
        if form.is_valid():
            m = form.save()
            self.success(m)
            return redirect(reverse('merchant-signup-success'))
        return render(request, self.template_name, 
                { 'form': form })

    def get(self, request):
        form = ArdLeadForm()
        context = dict(form=form, page_contact=1)
        return render(request, self.template_name, 
                context)

#-------------------------------------------------------------------------------- 

class MerchantsPage(TemplateResponseMixin, View):

    template_name = 'pages/merchants.html'

    '''Should be an even number - the number of merchants we will 
    feature on this page.'''
    merchant_num = 16

    def get(self, request):
        merchants = ArdMerchant.objects.filter(is_live=True)
        max_num = merchants.count()
        #if self.merchant_num < max_num:
            #max_num = self.merchant_num
        context = dict(merchants=[merchants[i] for i in xrange(max_num)],
                page_merchants=1)
        return render(request, self.template_name, context)

#-------------------------------------------------------------------------------- 

