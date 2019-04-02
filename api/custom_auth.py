from datetime import datetime

from rest_framework.exceptions import APIException

from api import models
from api.redis_pool import REDIS_CONN


# 验证Token
class Auth:

    def authenticate(self, request):
        token = request.data.get('token')
        if token:
            token, username = token.split('|')
            try:
                value = REDIS_CONN.get(username).decode('utf-8')
                if value:
                    if value == token:
                        return username, request
                raise APIException({'errors': '请先登录'})
            except Exception as e:
                print(e)
                tok = models.Token.objects.filter(user__username=username, token=token).first()
                if tok:
                    if tok.expired_time > datetime.now():
                        return username, request
                    else:
                        tok.delete()
                        raise APIException({'errors': '会话超时,请重新登陆'})
        raise APIException({'errors': '请先登录'})
