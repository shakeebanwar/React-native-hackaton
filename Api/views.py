from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from passlib.hash import django_pbkdf2_sha256 as handler
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# from .models import Signup,SerSignup,Request_Blood,SerRequest_Blood,Donate_Blood,SerDonate_Blood
from fcm_django.models import FCMDevice
from django.db.models import Q


class index(APIView):

    def get(self,request):

        
        return Response("ok")
