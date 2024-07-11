# from account.models import User
# from rest_framework import serializers
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.password_validation import validate_password


# class LoginSerializer(serializers.Serializer):
#     phone = serializers.CharField()
#     password = serializers.CharField()


# # class CreatUserSerializer(serializers.Serializer):
# #     first_name = serializers.CharField()
# #     last_name = serializers.CharField()
# #     username = serializers.CharField()
# #     password1 = serializers.CharField() 
# #     password2 = serializers.CharField()


# class ReadUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         exclude = ('password', 'user_permissions', 'groups')


# class CreatUserSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         exclude = ('password', 'user_permissions', 'groups', 'is_staff', 'is_active', 'is_superuser')

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError({'password2': ["Пароли не совпадают."]})
#         return data
    
#     # def validate_first_name(self, first_name):
#     #     return first_name

#     def create(self, validated_data):
#         password = validated_data.pop('password1')
#         validated_data.pop('password2')
#         validated_data['password'] = make_password(password)

#         return super().create(validated_data)
    
#     # def update(self, instance, validated_data):
#     #     return instance
from rest_framework import serializers
from account.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class CreatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'Idpassporta', 'organ_vidachi', 'personal_number_passport',
            'avatar', 'phone', 'email', 'role', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            Idpassporta=validated_data.get('Idpassporta', ''),
            organ_vidachi=validated_data.get('organ_vidachi', ''),
            personal_number_passport=validated_data.get('personal_number_passport', ''),
            avatar=validated_data.get('avatar', None),
            phone=validated_data['phone'],
            role=validated_data.get('role', User.CLIENT),
        )
        return user

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'Idpassporta', 'organ_vidachi', 'personal_number_passport',
            'avatar', 'phone', 'email', 'role'
        ]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
