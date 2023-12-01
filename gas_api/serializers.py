from rest_framework import serializers
from .models import Gas, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        

class GasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gas
        fields = '__all__'