#TEST TEST TEST
DEBUG = True
TEMPLATE_DEBUG = DEBUG
#LOGGING_OUTPUT_ENABLED = True

# Needed to enable compression JS and CSS files
COMPRESS = False
MEDIA_URL = '/static/'
MEDIA_ROOT = 'rooibos/static/'


ADMINS = (
#    ('Your name', 'your@email.example'),
)

MANAGERS = ADMINS

# Settings for MySQL
DATABASE_ENGINE = 'sqlite3'#'postgresql_psycopg2','postgresql'  , 'mysql', 'sqlite3' or 'oracle'.

DATABASES = { 
'default': {'ENGINE': 'django.db.backends.sqlite3', 
            'NAME': '/opt/vic-did/var/mdid-scratch/vic-did.db', #database name
            'USER': 'apache', #username for database
            'PASSWORD': '',
            'HOST':'', #set to empty for localhost
            'PORT':'' } } #empty for default

DATABASE_OPTIONS = {
#    'use_unicode': True,
#    'charset': 'utf8',
}

# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}

# Settings for all database systems
DATABASE_NAME = '/opt/vic-did/var/mdid-scratch/vic-did.db'             # Or path to database file if using sqlite3.
DATABASE_USER = 'rooibos'             # Not used with sqlite3.
DATABASE_PASSWORD = 'rooibos'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'NZ'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e#!poDuIJ}N,".K=H:T/4z5POb;Gl/N6$6a&,(DRAHUF5c",_p'

#STATIC_URL = '/static'
ADMIN_MEDIA_PREFIX = '/static/admin/'

SOLR_URL = 'http://127.0.0.1:8983/solr/'

SCRATCH_DIR = '/opt/vic-did/var/mdid-scratch/'
AUTO_STORAGE_DIR = '/opt/vic-did/var/mdid-collections/'

# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

INTERNAL_IPS = ('127.0.0.1',)

HELP_URL = 'http://mdid.org/help/'

DEFAULT_LANGUAGE = 'en-us'

GOOGLE_ANALYTICS_MODEL = True

FLICKR_KEY = 'cf6c8e01f6c468dd8be08f4c68e5fd0e'
FLICKR_SECRET = '4e758a1ea794e497'

# Set to None if you don't subscribe to ARTstor
ARTSTOR_GATEWAY = None
#ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'

OPEN_OFFICE_PATH = 'C:/Program Files/OpenOffice.org 3/program/'

GEARMAN_SERVERS = ['127.0.0.1']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
#    'rooibos.auth.ldapauth.LdapAuthenticationBackend',
#    'rooibos.auth.mailauth.ImapAuthenticationBackend',
    'rooibos.auth.mailauth.PopAuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'rooibos.auth.middleware.BasicAuthenticationMiddleware',
)

LDAP_AUTH = (
    {
        'uri': 'ldap://ldap.example.edu',
        'base': 'ou=People,o=example',
        'cn': 'cn',
        'version': 2,
        'scope': 1,
        'options': {'OPT_X_TLS_TRY': 1},
        'attributes': ('sn', 'mail', 'givenName', 'eduPersonPrimaryAffiliation'),
        'firstname': 'givenname',
        'lastname': 'sn',
        'email': 'mail',
    },
)

IMAP_AUTH = (
    {
        'server': 'imap.example.edu',
        'port': 993,
        'domain': 'example.edu',
        'secure': True,
    },
)

POP_AUTH = (
    {
        'server': 'pop.gmail.com',
        'port': 995,
        'domain': 'gmail.com',
        'secure': True,
    },
)

SESSION_COOKIE_AGE = 6 * 3600  # in seconds

SSL_PORT = None  # ':443'

# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"

CUSTOM_TRACKER_HTML = ""

EXPOSE_TO_CONTEXT = ('STATIC_DIR', 'PRIMARY_COLOR', 'SECONDARY_COLOR', 'CUSTOM_TRACKER_HTML', 'ADMINS')

# The Megazine viewer is using a third party component that has commercial
# licensing requirements.  To enable the component you need to enter your
# license key, which is available for free for educational institutions.
# See static/megazine/COPYING.
MEGAZINE_PUBLIC_KEY = ""

# To use a commercial licensed flowplayer, enter your flowplayer key here
# and add the flowplayer.commercial-3.x.x.swf file to the
# rooibos/static/flowplayer directory
FLOWPLAYER_KEY = ""

# MDID uses some Yahoo APIs that require an application key
# You can get one at https://developer.apps.yahoo.com/dashboard/createKey.html
YAHOO_APPLICATION_ID = ""

DIGITALNZ_KEY = "xkwXgnxgnmyUbAFU1VqZ"

# By default, video delivery links are created as symbolic links. Some streaming
# servers (e.g. Wowza) don't deliver those, so hard links are required.
HARD_VIDEO_DELIVERY_LINKS = False

additional_settings = [
#    'apps.jmutube.settings_local',
#    'apps.svohp.settings_local',
]

UPLOAD_LIMIT = 999999999
