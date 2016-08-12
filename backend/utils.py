import jwt
import boto3
import requests
from django.conf import settings

class UserProfileClass(object):
    '''
    '''
    def get_user_profile(self, access_token):
        '''
        '''
        user_url = "https://{domain}/userinfo?access_token={access_token}"  \
        .format(domain='delhivery-org.auth0.com', access_token=access_token)
        
        user_info = requests.get(user_url).json()
        return user_info
    
    def get_or_save_user_profile(self, user_info):
        '''
        '''
        if user_info.get('email'):
            user_profile, created = UserProfile.objects.get_or_create(email=user_info['email'])
            
        else:
            user_profile, created = UserProfile.objects.get_or_create(phone_number=user_info['phone_number'])
        return user_profile, created

    def get_or_save_related_profile(self, user, user_info, connection_type):
        '''
        '''
        related_profile, created = RelatedProfile.objects.get_or_create(user=user,
                                                                        connection_type=connection_type)
        related_profile.data = user_info
        related_profile.autho_id = user_info['user_id']
        related_profile.save()
        return user

    def validate_jwt_token(self, token):
        '''
        '''
        secret = settings.AUTHO_SECRET_KEY
        payload = jwt.decode(str(token), 
                             secret, algorithms=['HS256'],options = {
                                                           'verify_signature': False,
                                                           'verify_exp': True,
                                                           'verify_nbf': True,
                                                           'verify_iat': True,
                                                           'verify_aud': False,
                                                           'require_exp': False,
                                                           'require_iat': False,
                                                           'require_nbf': False
                                                           })
        return payload
