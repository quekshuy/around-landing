import os

# Hat tip http://justcramer.com/2011/01/13/settings-in-django/
# import global defaults

import sys
PROJECT_ROOT = os.path.split(os.path.abspath(__file__))[0]
LIBS_PATH = os.path.join(PROJECT_ROOT, 'lib')
APPS_PATH = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(0, APPS_PATH)
sys.path.append(LIBS_PATH)

from conf.settings.default import *

# Also append the project's specific libraries to the path

DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

# import local settings
try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write(
    "Warning: Can't find the file 'local_settings.py' " 
    "in the directory containing %r. It appears you've customized "
    "things.\nYou'll have to run django-admin.py, passing it your "
    " settings module.\n(If the file settings.py does indeed exist, it's "
    "causing an ImportError somehow.)\n" % __file__) 
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()

#  -----  Specific to ep.io -------

TEMPLATE_DIRS = (
            os.sep.join([PROJECT_ROOT, 'templates'])
        )


# ----- End ep.io -------

# remove disabled apps

if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    #DATABASE_ROUTERS = list(DATABASE_ROUTERS)
    #TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)

    #for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
        #if m.startswith(a):
            #TEMPLATE_CONTEXT_PROCESSORS.pop(x)

    #for x, m in enumerate(DATABASE_ROUTERS):
        #if m.startswith(a):
            #DATABASE_ROUTERS.pop(x)


