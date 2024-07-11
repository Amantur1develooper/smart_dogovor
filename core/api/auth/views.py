# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.contrib.auth import authenticate
# from rest_framework import status
# from .serializers import LoginSerializer, ReadUserSerializer, CreatUserSerializer
from rest_framework.authtoken.models import Token


# @api_view(['POST'])
# def register_api_view(request):
#     serializer = CreatUserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
#     token, created = Token.objects.get_or_create(user=user)
#     read_serializer = ReadUserSerializer(user, context={'request': request})
#     data = {**read_serializer.data, 'token': token.key}
#     return Response(data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def login_api_view(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     phone = serializer.validated_data.get('phone')
#     password = serializer.validated_data.get('password')

#     user = authenticate(phone=phone, password=password)

#     if user:
#         token, created = Token.objects.get_or_create(user=user) # (token, False)
#         read_serializer = ReadUserSerializer(user, context={'request': request})
#         data = {**read_serializer.data, 'token': token.key}
#         return Response(data)

#     return Response(    
#         {'detail': 'Не существует пользователя или неверный пароль.'}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from account.models import User
from .serializers import LoginSerializer, ReadUserSerializer, CreatUserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreatUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user) # (token, False)
        read_serializer = ReadUserSerializer(user, context={'request': request})
        data = {**read_serializer.data, 'token': token.key}
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            # refresh = RefreshToken.for_user(user)
            token, created = Token.objects.get_or_create(user=user) # (token, False)
            read_serializer = ReadUserSerializer(user, context={'request': request})
            data = {**read_serializer.data, 'token': token.key}
            return Response(data)
            # read_serializer = ReadUserSerializer(user, context={'request': request})
            # data = {**read_serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token)}
            # return Response(data)
        
        return Response({'detail': 'Не существует пользователя или неверный пароль.'}, status=status.HTTP_401_UNAUTHORIZED)