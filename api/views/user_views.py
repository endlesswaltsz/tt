import datetime
import hashlib


from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.redis_pool import REDIS_CONN
from api.serialiazer import response


def get_token(username):
    m = hashlib.md5()
    m.update((username + str(datetime.datetime.now())).encode('utf-8'))
    return m.hexdigest()


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            token = get_token(username)
            expired_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
            try:
                models.Token.objects.update_or_create(user=user,
                                                      defaults={'token': token, 'expired_time': expired_time})
                REDIS_CONN.set(username, token, ex=120)
                response.status=100
                response.msg = {'token':token + '|' + username,'username':username}

            except Exception as e:
                print(e)
                response.status = 101
                response.msg = '未知错误'
        else:
            response.status = 101
            response.msg = '帐号或密码错误'
        return Response(response.response)
