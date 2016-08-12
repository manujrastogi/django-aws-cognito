import requests
import boto3
import json
import jwt
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from backend.utils import UserProfileClass


class SignUp(APIView):
    '''
    '''
    def post(self, request, *ars, **kwargs):
        '''
        '''
        idp_client = boto3.client('cognito-idp', **settings.DEFAULT_CONFIG)
        user = idp_client.sign_up(ClientId=settings.DEFAULT_USER_POOL_APP_ID,
                                Username=request.data['username'],
                                Password=request.data['password'])
        return Response(data={'user':user}, status=status.HTTP_201_CREATED)


class AdminInitiateAuth(APIView):
    '''
    '''
    def post(self, request, *args, **kwargs):
        '''
        '''
        idp_client = boto3.client('cognito-idp', **settings.DEFAULT_CONFIG)
        ci_client = boto3.client('cognito-identity', **settings.DEFAULT_CONFIG)
        user = idp_client.admin_initiate_auth(UserPoolId=settings.DEFAULT_USER_POOL_ID,
                                       AuthFlow='ADMIN_NO_SRP_AUTH', 
                                       ClientId=settings.DEFAULT_USER_POOL_APP_ID, 
                                       AuthParameters={'USERNAME':request.data['username'], 
                                                       'PASSWORD':request.data['password']}
                                       )
        # get identity id
        res = ci_client.get_id(AccountId=settings.ACCOUNTID,
                                IdentityPoolId=settings.IDENTITYPOOLID,
                                Logins={
                                        settings.DEFAULT_USER_POOL_LOGIN_PROVIDER:user['AuthenticationResult']['IdToken']
                                        }
                                )
        return Response(data={'user':user,
                              'res':res}, status=status.HTTP_201_CREATED)

    
class PublicProviderLogin(APIView):
    '''
    '''
    def post(self, request, *args, **kwargs):
        '''
        '''
        token = request.data['token']
        provider = request.data['provider']
        ci_client = boto3.client('cognito-identity', **settings.DEFAULT_CONFIG)
        # check the user if it exists in USER POOL
        
        # get identity id
        res = ci_client.get_id(AccountId=settings.ACCOUNTID,
                                IdentityPoolId=settings.IDENTITYPOOLID,
                                Logins={
                                        provider:token
                                        }
                                )
        return Response(data={'res':res}, status=status.HTTP_201_CREATED)
        
        
        
        
        
