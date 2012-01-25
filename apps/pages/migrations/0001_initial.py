# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ArdMerchant'
        db.create_table('pages_ardmerchant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('card_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('pages', ['ArdMerchant'])


    def backwards(self, orm):
        
        # Deleting model 'ArdMerchant'
        db.delete_table('pages_ardmerchant')


    models = {
        'pages.ardmerchant': {
            'Meta': {'object_name': 'ArdMerchant'},
            'card_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pages']
