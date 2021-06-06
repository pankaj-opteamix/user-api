from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework import viewsets,status
from .serializers import UsersSerializer
from .models import Users
from .utils import request_user_handler
from .users import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        users = Users.objects.all()
        print(users)
        if not users:
            return Response({'errorResponse': 'No obect is found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(users,context={'request': request},many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    @request_user_handler
    def create(self, request):
        if not request.data:
            return Response({'errorResponse': 'invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user=User()
            boolobj,msg=user.create_user(request)
            if boolobj:
                serializer = UsersSerializer(data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'errorResponse': 'Server Internal Error Occured = ' + repr(e)},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )
            else:
                return Response({'errorResponse': msg}, status=status.HTTP_400_BAD_REQUEST)




    def retrieve(self, request,pk=None):
        users = self.queryset.filter(pk=pk)
        if not users:
            return Response({'errorResponse': 'Object id %s not found' % pk}, status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        serializer = UsersSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



    def update(self, request, pk=None,partial=False):
        print(pk)
        users = self.queryset.filter(pk=pk)
        if not users:
            return Response({'errorResponse': 'Object id %s not found' % pk},
                    status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        serializer = UsersSerializer(data=request.data, context={'request': request}, partial=partial, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errorResponse': serializer.errors, 'type': 'serializer'}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk=None,partial=True):
        print(pk)
        users = self.queryset.filter(pk=pk)
        print(users)
        if not users:
            return Response({'errorResponse': 'Object id %s not found' % pk},
                            status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        serializer = UsersSerializer(data=request.data, context={'request': request}, partial=partial, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errorResponse': serializer.errors, 'type': 'serializer'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, p=None):
        user_objs = Users.objects.filter(pk=pk)
        if not user_objs:
            return Response({'errorResponse': 'Object id %s not found' % pk},
                    status=status.HTTP_404_NOT_FOUND)
        user= user_objs.get()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



