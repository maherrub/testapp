from .base import *
#from .storage_backends import *

DEBUG = False

ADMINS = (
	('maherrub', 'maher@live.com.sg'),
)

ALLOWED_HOSTS = ['127.0.0.1',
                'http://testappapp.nedccmpyec.ap-southeast-1.elasticbeanstalk.com', 
                'testappapp.nedccmpyec.ap-southeast-1.elasticbeanstalk.com',
                'http://ip-172-31-25-204.ap-southeast-1.compute.internal',
                'ip-172-31-25-204.ap-southeast-1.compute.internal',
                'https://testapp-static.s3.amazonaws.com',
                'testapp-static.s3.amazonaws.com',]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {'charset': 'utf8mb4'},
        'NAME': 'testdb',
		'USER': 'testdba',
		'PASSWORD': 'testdba_admin',
		'HOST': 'testdbinstance.ccoelatjjhl3.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',  
    }
}


# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'testappapp.nedccmpyec.ap-southeast-1.elasticbeanstalk.com:11211',
    }
}

# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

AWS_ACCESS_KEY_ID = 'AKIAIH4FVFYZDHKVYSOA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'testapp-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)


# Media storage
#DEFAULT_FILE_STORAGE = 'settings.storage_backends.MediaStorage'  # <-- here is where we reference it


#STATICFILES_LOCATION = 'static' 
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


