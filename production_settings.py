from settings import *

# Specific to ep.io
import os
from bundle_config import config
MEDIA_ROOT = os.sep.join([config['core']['data_directory'], 'uploads/']) 
