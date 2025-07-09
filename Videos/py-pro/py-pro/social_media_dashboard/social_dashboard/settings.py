from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key'

# DEVELOPMENT KE LIYE DEBUG TRUE RAKHO
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'social_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_dashboard.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ✅ Social Auth Backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)


# ✅ Twitter App Credentials
SOCIAL_AUTH_TWITTER_KEY = 'ADD_TWITTER_KEY'
SOCIAL_AUTH_TWITTER_SECRET = 'ADD_TWITTER_SECRET'

# ✅ Custom API Tokens for Real-Time Fetch
TWITTER_BEARER = 'ADD_TWITTER_BEARER_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# FB_ACCESS_TOKEN = 'EAArM5UW023IBO97JMgnAXMuJqKFUwHnCBVZAnIwQ6AtnSzzQHDL9fNF2wa0ZB2LdkQodCUxf0DAcO6xD2QceveSSNpZCgt1DhAZBaWDZCi9k8DV1KDNWZCHNly7txLZC52TdVLBQnuAv5itIWreqSZB5w6bjTxDXdmy4MGEeFDhhzsxfsG2q7ZBiphxpmma0x'
LOGIN_URL = '/login/'




# Add your secret keys safely
# OAuth 1.0a Keys for Posting Tweets
TWITTER_CONSUMER_KEY = 'ADD_TWITTER_CONSUMER_KEY_xxxxxxxxxxxxxxxxxxxxxxxxjZzjVGHo'
TWITTER_CONSUMER_SECRET = 'ADD_ZVfVXNxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWITTER_ACCESS_TOKEN = 'ADD_TWITTER_ACCESS_TOKENxxxxxxxxxxxxxxxxxxxxxxxxxxxx9FUuYa7jjJhrpfhS1'
TWITTER_ACCESS_TOKEN_SECRET = 'ADD_TWITTER_ACCESS_TOKEN_SECRET9RssGmCxxxxxxxxxxxxxxxxxxxxxxOmbfhkpp0uuqBbe'

# Optional - Agar Bearer Token mila hai for Read-Only Endpoints


TWITTER_BEARER = 'ADD_TWITTER_BEARER_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxhjDrb4xpVUfPwQkfDnEwHrvhdh18p'




# Facebook Developer App Details
SOCIAL_AUTH_FACEBOOK_KEY = 'ADD_FACEBOOK_KEY_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx7dddddddddddd299'
SOCIAL_AUTH_FACEBOOK_SECRET = 'aDD_FACEBOOK_KEY2xxxxxxxxxxxxxxxxxx1f2'



# FB Access Token & Page ID (Temporary - Better is to fetch dynamically)
FB_ACCESS_TOKEN = 'ADD_FB_ACCESS_TOKENxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxAAKTj4Ev720CyuzK6RnpEGRpGd31ll6xxxxxxxxxxte3E4PhZAeJZClX19Q2ihts0elC6fGmmN5ww'
FB_PAGE_ID = 'ADD_FB_PAGE_ID74fwswssdaa438'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'