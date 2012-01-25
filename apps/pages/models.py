
import os
from django.db import models
from django.template.defaultfilters import slugify

#-------------------------------------------------------------------------------- 

def upload_merchant_image(instance, filename):
    return os.sep.join([ 'merchants',
        slugify(instance.name),
        'brand-' + filename
        ])

#-------------------------------------------------------------------------------- 

class ArdMerchant(models.Model):
    class Meta:
        verbose_name = 'Merchant'
    name = models.CharField(max_length=128, blank=False, null=False)
    card_image = models.ImageField(upload_to=upload_merchant_image)
    website = models.URLField()
    is_live = models.BooleanField(default=True)

    def __unicode__(self):
        return ', '.join([self.name,  'is_live: %s' % str(self.is_live)])

