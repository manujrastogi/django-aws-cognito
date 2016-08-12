# django-aws-cognito
AWS cognito identity and cognito identity provider sample project

#Setup steps:

1. pip install -r requirements.pip
2. python manage.py migrate
3. python manage.py runserver


#Things to change:

1. home.html - google-signin-client_id in meta tag.

2. setup a local_settings.py and specify the following variables:

AWS COGNITO CREDENTIALS

IDENTITYPOOLID = ''

ACCOUNTID = ''

AWS_ACCESS_KEY = ''

AWS_SECRET_KEY = ''

DEFAULT_REGION_NAME = ''

DEFAULT_USER_POOL_ID = ''

DEFAULT_USER_POOL_APP_ID = '' #APP should not have any secret in AWS

DEFAULT_CONFIG = {'region_name':DEFAULT_REGION_NAME,
                  'aws_access_key_id':AWS_ACCESS_KEY,
                  'aws_secret_access_key':AWS_SECRET_KEY}

DEFAULT_USER_POOL_LOGIN_PROVIDER = ''
