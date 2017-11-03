from .base import *

DEBUG = False

ADMINS = (
	('maherrub', 'maher@live.com.sg'),
)

ALLOWED_HOSTS = ['127.0.0.1','http://testappapp.nedccmpyec.ap-southeast-1.elasticbeanstalk.com', 'testappapp.nedccmpyec.ap-southeast-1.elasticbeanstalk.com']

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
