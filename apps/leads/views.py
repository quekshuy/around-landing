
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages

from models import ArdLead
from forms import (
        ArdLeadBasicsForm, 
        ArdLeadMerchantForm, 
        ArdLeadImagesForm
        )

#-------------------------------------------------------------------------------- 
class ArdLeadError(Exception):
    '''Specific to our uses'''
    pass

#-------------------------------------------------------------------------------- 

class SubmitArdLeadView(TemplateResponseMixin, View):
    '''
        Handles a form submission for an ArdLead.
        Future: will use an email service to send an email out, 
        to inform the sales team.
    '''
    template_name = 'pages/merchant_signup.html'
    success_template = 'pages/merchant_signup_success.html'
    error_template = 'pages/merchant_signup_fail.html'

    PARAM_MODEL_ID = 'mid'
    PARAM_FORM = 'form'
    model = ArdLead

    def get_instance(self, mid):
        inst = None
        try:
            inst = self.model.objects.get(id=long(mid))
        except self.model.DoesNotExist:
            pass
        return inst
            
    def _process_image_form(self, request):
        context = {'step_number': 2 }
        inst = self.get_instance(request.session[self.PARAM_MODEL_ID])
        if not inst:
            return redirect(reverse('merchant-signup-error'))
        if request.POST:
            form = ArdLeadImagesForm(request.POST, request.FILES, 
                    instance=inst)
            if form.is_valid():
                form.save()
                del request.session[self.PARAM_MODEL_ID]
                return redirect(reverse('merchant-signup-success'))
        else:
            form = ArdLeadImagesForm()
        context[self.PARAM_FORM] = form
        return render(request, self.template_name, 
                context)

    def _process_merchant_form(self, request):
        context = {'step_number': 1}
        print request.session[self.PARAM_MODEL_ID]
        inst = self.get_instance(request.session[self.PARAM_MODEL_ID])
        if not inst:
            return redirect(reverse('merchant-signup-error'))
        elif request.POST:
            form = ArdLeadMerchantForm(request.POST, instance=inst)
            if form.is_valid():
                form.save()
                return redirect(reverse('merchant-signup-middle', 
                    kwargs={ 'step_number' : 2 }))
        else:
            form = ArdLeadMerchantForm()
        context[self.PARAM_FORM] = form
        return render(request, self.template_name, 
                context)

    def _process_basic_form(self, request):
        context = {'step_number': 0 }
        if request.POST:
            form = ArdLeadBasicsForm(request.POST)
            if form.is_valid():
                m = form.save()
                request.session[self.PARAM_MODEL_ID] = m.id
                return redirect(reverse('merchant-signup-middle',
                    kwargs={'step_number': 1}))
        else:
            form = ArdLeadBasicsForm()
        context[self.PARAM_FORM] = form
        return render(request, self.template_name,
                context)

    def post(self, request, step_number=0):
        '''Handle a POST request - form submission'''
        fns = [ 
                self._process_basic_form,
                self._process_merchant_form,
                self._process_image_form ]

        step_number = long(step_number)
        print 'Step number: %d' % step_number
        if step_number >= len(fns):
            return redirect(reverse('merchant-signup-error'))
        return fns[step_number](request)


    def get(self, request, step_number=0):
        '''
            We've devolved to using sessions because 
            we want to have the model instance transferred
            between each form-page.
        '''
        forms = [   ArdLeadBasicsForm,
                    ArdLeadMerchantForm,
                    ArdLeadImagesForm 
                ]
        # Convert to integer
        step_number = long(step_number)
        if step_number == 0:
            request.session.set_test_cookie()
            # For testing of message bar
            #messages.add_message(request, 
                    #messages.ERROR, 
                    #'Just a test message.')

        if step_number > len(forms):
            pass # Return a 404 error

        form = forms[step_number]()
        if step_number:
            if step_number == 1 and \
                    request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            elif step_number == 1:
                messages.add_message(request, messages.ERROR, 
                        'Sorry but you need to enable cookies '
                        'in your browser for sign up to take place.')

        mid = request.session.get('mid', None)
        kw = dict()
        if mid:
            inst = self.get_instance(mid)
            if inst: 
                for f in form.fields:
                    if hasattr(inst, f):
                        kw[f] = getattr(inst, f)
                # Set the initial fields
                kw = {'initial' : kw }
        form = forms[step_number](**kw)
        return render(request, self.template_name, 
                { 'form': form,
                    'step_number': step_number } )

#-------------------------------------------------------------------------------- 

