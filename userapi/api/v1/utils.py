import functools
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def request_user_handler(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        req_obj = args[1]
        logger.info("validing user Authentication")
        USERNAME = 'admin'
        PASSWORD = 'admin1234'
        if USERNAME == req_obj.META['HTTP_USERNAME'] and PASSWORD == req_obj.META['HTTP_PASSWORD']:
            logger.info("Authoriztion approved")
            result = f(*args, **kwargs)
            return result
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)





    return wrapper
