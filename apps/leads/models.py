import os
import datetime
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

#-------------------------------------------------------------------------------- 

def lead_upload_to(field=''):
    '''Wrapper for a function that specifies the upload
    path for a lead's image'''
    def _upload_to(instance, filename):
        return os.sep.join([settings.MEDIA_ROOT, 
            datetime.date.today().strftime('%d%m%Y'),
            slugify(instance.brand_name), 
            slugify(instance.name),
            field, filename])
    return _upload_to

#-------------------------------------------------------------------------------- 

class ArdLead(models.Model):
    '''
        This is a lead that we will try to contact.
    '''
    name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=128, blank=False, null=False)
    contact_number = models.PositiveIntegerField(blank=False, null=False)
    brand_name = models.CharField(max_length=128, blank=False, null=False)

    """Optional address for entry"""
    outlet_address = models.CharField(max_length=255, blank=True, null=True)

    """All the promo mechanics and loyalty program mechanics"""
    mechanics_desc = models.TextField(blank=True, null=True)

    """Brand image"""
    brand_image = models.ImageField(upload_to=lead_upload_to(field='brand'))

    """Product image"""
    product_image = models.ImageField(upload_to=lead_upload_to(field='product'))

    def __unicode__(self):
        return ', '.join([self.name, self.email])

#-------------------------------------------------------------------------------- 
