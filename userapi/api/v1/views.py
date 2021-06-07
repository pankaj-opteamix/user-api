from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework import viewsets,status
from .serializers import UsersSerializer
from .models import Users
from .utils import request_user_handler
from .users import User
import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @request_user_handler
    def list(self, request):
        """List all the users"""
        logger.info("Fetching List of Users")
        users = Users.objects.all()
        if not users:
            logger.error('No User exist!')
            return Response({'errorResponse': 'No obect is found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(users,context={'request': request},many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    @request_user_handler
    def create(self, request):
        """create a new user """
        if not request.data:
            logger.error('Bad request  validate your data before sending')
            return Response({'errorResponse': 'invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user=User()
            logger.info("creating user and checking email validation")
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

    @request_user_handler
    def retrieve(self, request,pk=None):
        """get user object by  primary key """
        logger.info("inside get retrieve function")
        users = self.queryset.filter(pk=pk)
        if not users:
            logger.error('No User exist for this id')
            return Response({'errorResponse': 'Object id %s not found' % pk}, status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        logger.info("searlizing user data for single usere")
        serializer = UsersSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @request_user_handler
    def update(self, request, pk=None,partial=False):
        """update the  user object or create a new object if user object does not exist """
        users = self.queryset.filter(pk=pk)
        logger.info("inside update function")
        if not users:
            logger.error('No User exist for this id')
            return Response({'errorResponse': 'Object id %s not found' % pk},
                    status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        logger.info("inside update view searlizing user data for single usere")
        serializer = UsersSerializer(data=request.data, context={'request': request}, partial=partial, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errorResponse': serializer.errors, 'type': 'serializer'}, status=status.HTTP_400_BAD_REQUEST)

    @request_user_handler
    def partial_update(self, request,pk=None,partial=True):
        """partial update for the  user object """
        users = self.queryset.filter(pk=pk)
        logger.info("inside partial update function ")
        if not users:
            logger.error('No User exist for this id')
            return Response({'errorResponse': 'Object id %s not found' % pk},
                            status=status.HTTP_404_NOT_FOUND)
        user = users.get()
        serializer = UsersSerializer(data=request.data, context={'request': request}, partial=partial, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errorResponse': serializer.errors, 'type': 'serializer'}, status=status.HTTP_400_BAD_REQUEST)

    @request_user_handler
    def delete(self, request, pk=None, p=None):
        """destroying the user object """
        logger.info("inside delete function ")
        user_objs = Users.objects.filter(pk=pk)
        if not user_objs:
            logger.error('No User exist for this id')
            return Response({'errorResponse': 'Object id %s not found' % pk},
                    status=status.HTTP_404_NOT_FOUND)
        user= user_objs.get()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



