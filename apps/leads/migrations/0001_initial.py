# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ArdLead'
        db.create_table('leads_ardlead', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('contact_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('brand_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('outlet_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mechanics_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('brand_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('product_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('leads', ['ArdLead'])


    def backwards(self, orm):
        
        # Deleting model 'ArdLead'
        db.delete_table('leads_ardlead')


    models = {
        'leads.ardlead': {
            'Meta': {'object_name': 'ArdLead'},
            'brand_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'contact_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mechanics_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'outlet_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['leads']
