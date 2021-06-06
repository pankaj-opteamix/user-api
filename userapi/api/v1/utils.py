import functools
from rest_framework.response import Response
from rest_framework import status
def request_user_handler(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        req_obj = args[1]
        (req_obj.META['HTTP_USERNAME'])
        if req_obj.data:
            print("inside request")
            result = f(*args, **kwargs)
            return result
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)





    return wrapper
