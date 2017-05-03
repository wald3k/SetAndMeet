"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eplib=kr-zy_x$1-rsn)2+cx3_=8&-7theah($(ekgk(0gp%8o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites', #for setting domain name
    'django.contrib.staticfiles',
    #----------- third party apps -----------
    'Event',
    'Profile',
    #'Message',
    'Comment',
    'geoposition',
    'Location',
    'django_messages',
    'social.apps.django_app.default',
    'django_extensions', #for graphviz
    'Shout',
    #'rest_framework', #adding django-rest-framework
    'RatingSystem',#for EventRating & ProfileRating
    'django.contrib.humanize',#possible to write in django-templates: {{ event.end_date|naturaltime|capfirst }}. Also dont forget to {% load humanize %} in a template file.
]
#After adding 'django.contrib.sites', to installed apps
SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        BASE_DIR + '/templates/',
        os.path.join(BASE_DIR,'Event'),
        os.path.join(BASE_DIR,'Profile'),
        os.path.join(BASE_DIR,'Person'),

        #'/home/wald/Desktop/wsLic/myEnv/lib/python2.7/site-packages/django_messages',
        #"/home/wald/Desktop/wsLic/myEnv/lib/python2.7/site-packages/geoposition/templates/geoposition"

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #third party apps
                #'django_messages.context_processors.inbox',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.core.context_processors.request' #needed to acces {{ request.user }}
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'


#These STATICFILES_DIRS are common for all applications!
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]

#my changes

#geoposition SETTINGS
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyApgBwHhWwbYLOLuj_0Dv3hMbkT6oM7a_0'
GEOPOSITION_MAP_WIDGET_HEIGHT = 300
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 20,
}
GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}
#geoposition SETTINGS END

#Social auth settings start
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)



SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/login_secondary/'
LOGIN_URL = '/login_secondary/'
#SOCIAL_AUTH_ALWAYS_ASSOCIATE = True
#LOGIN_ERROR_URL = '/error/'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}

SOCIAL_AUTH_FACEBOOK_KEY = 689314807884596 #make sure this number is not in 'quotes'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b968efbba34a3995b5350756b9f65f6f'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    #'Profile.pipeline.save_profile'
    'Profile.pipeline.get_avatar',
)
#Social auth settings end
SESSION_COOKIE_AGE = 1209600 #Defining Django session cookie age in seconds 1209600(2 weeks, in seconds)
