import datetime
from typing import Dict

import jwt




SALT = "showMaker"

def create_token(payload: Dict, timeout= 1):

    headers = {
        'alg': "HS256",
        'typ': "jwt"
    }

    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=2)

    result = jwt.encode(headers=headers, payload=payload, key=SALT, algorithm="HS256")
    return result