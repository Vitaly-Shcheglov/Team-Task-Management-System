import datetime

import jwt


def generate_token(user):
    payload = {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    from django.conf import settings

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token
