# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ArdLead.brand_name'
        db.alter_column('leads_ardlead', 'brand_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'ArdLead.brand_image'
        db.alter_column('leads_ardlead', 'brand_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'ArdLead.product_image'
        db.alter_column('leads_ardlead', 'product_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'ArdLead.brand_name'
        db.alter_column('leads_ardlead', 'brand_name', self.gf('django.db.models.fields.CharField')(default='Acme', max_length=128))

        # User chose to not deal with backwards NULL issues for 'ArdLead.brand_image'
        raise RuntimeError("Cannot reverse this migration. 'ArdLead.brand_image' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ArdLead.product_image'
        raise RuntimeError("Cannot reverse this migration. 'ArdLead.product_image' and its values cannot be restored.")


    models = {
        'leads.ardlead': {
            'Meta': {'object_name': 'ArdLead'},
            'brand_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'contact_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mechanics_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'outlet_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['leads']
