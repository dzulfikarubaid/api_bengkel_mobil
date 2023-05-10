from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import ServisModel

class ServisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServisModel
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email':{
                'required':True,
                'allow_blank':False,
                'validators':[validators.UniqueValidator(User.objects.all(), "Email already exists")]

            }

        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)

        return user