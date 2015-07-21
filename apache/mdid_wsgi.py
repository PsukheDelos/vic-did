import os
import sys

activate_this = '/opt/vic-did/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

path = '/opt/vic-did'
path2 = '/opt/vic-did/rooibos'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append(path2)


os.environ['DJANGO_SETTINGS_MODULE'] = 'rooibos.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

