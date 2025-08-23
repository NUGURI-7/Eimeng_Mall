import datetime

import jwt

SALT = "nuguri"

def create_token():
    headers = {
        'alg': "HS256",
        'typ': "jwt"
    }
    payload = {
        'user_id': 1,
        'username': 'yefan',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }

    result = jwt.encode(headers=headers, payload=payload,key=SALT, algorithms="HS256")
    return result

# 解码token
def get_payload(token):
    try:
        o_result = jwt.decode(token, SALT, algorithms=["HS256"])
        return o_result
    except jwt.exceptions.DecodeError as e:
        print(e)
    except jwt.exceptions.ExpiredSignatureError as e:
        print(e)







if __name__ == "__main__":
    # token = create_token()
    # print(token)
    o_ = get_payload("eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InllZmFuIiwiZXhwIjoxNzU1NDM2NDg4fQ.qiM33D1mXkqLOTHTMwRozGmR43gf9tGnoDEDmUnzOIE")
    print(o_)