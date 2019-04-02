import datetime
import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from api import models
from api.custom_auth import Auth
from api.redis_pool import REDIS_CONN
# from api.serialiazer import CourseSerializer


# Create your views here.



# class Login(APIView):
#
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         obj = models.UserInfo.objects.filter(username=username, password=password)
#         if obj:
#             token = get_token(username)
#             REDIS_CONN.set(username, token, ex=60 * 60 * 24 * 2)
#             return Response({'status': 100, 'token': token + '|' + username})
#         return Response({'status': 101, 'errors': '帐号或密码错误'})
#
#
#
#
# class TEST(APIView):
#     def get(self,request,*args,**kwargs):
#         obj=models.FreeCourse.objects.filter(pk=1).first()
#         models.PricePolicy.objects.create()
#         return HttpResponse('ok')