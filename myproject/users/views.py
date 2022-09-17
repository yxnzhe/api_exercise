from django.http import Http404
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers

class registerUserViewSet(ViewSet):
    def create(self, request):
        inputData = {
            'name': request.data['name'],
            'username': request.data['username'],
            'email': request.data['email'],
            'password': make_password(request.data['password'], None, 'pbkdf2_sha256'), # Hashing password with SHA256
        }
        serializer = UserSerializers(data=inputData)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'User created successfully',
            'status': 201,
            'infomation': serializer.data
        }
        return Response(response)
class loginUserViewSet(ViewSet):
    def get_credential(self, email):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            raise Http404

    def create(self, request):
        email = request.data['email']
        user = self.get_credential(email)

        if(user.is_deleted == False): # Check if user's account still valid
            if(check_password(request.data['password'], user.password)):
                update_last_login(None, user) # Update last login date time

                serializer = UserSerializers(user, many=False)

                response = {
                    'username': serializer.data['username'],
                    'last_login': serializer.data['last_login'],
                    'status': 200
                }

                return Response(response)
            else:
                response = {
                    'message': 'Incorrect email or password',
                    'status': 401
                }
                return Response(response)
        else:
            raise Http404

class getAllUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
