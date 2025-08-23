import datetime
from typing import Dict

import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request


SALT = "showMaker"


def create_token(payload: Dict, timeout=1):
    headers = {
        'alg': "HS256",
        'typ': "jwt"
    }

    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=2)

    result = jwt.encode(headers=headers, payload=payload, key=SALT, algorithm="HS256")
    return result


def get_payload(token):
    result = {"status": False, "data": None, "error": None}

    try:
        payload = jwt.decode(token, SALT, algorithms=["HS256"])
        result["status"] = True
        result["data"] = payload
    except jwt.exceptions.DecodeError:
        print('token认证失败了')
        result["error"] = 'token认证失败'
    except jwt.exceptions.ExpiredSignatureError:
        print('token已经失效了')
        result["error"] = 'token已失效'
    except jwt.exceptions.InvalidTokenError:
        print('无效的,非法的token')
        result["error"] = '无效,非法token'
    return result


# 验证类
# 用户在url中进行token的参数配置

class JwtQueryParamAuthorization(BaseAuthentication):

    def authenticate(self, request: Request):
        token = request.query_params.get("token")
        result_payload = get_payload(token)
        print(result_payload)
        return result_payload,token

# header 携带token
class JwtAuthorization(BaseAuthentication):

    def authenticate(self, request: Request):
        token = request.META.get('HTTP_TOKEN')
        print(token)
        result_payload = get_payload(token)
        print(result_payload)
        return result_payload,token