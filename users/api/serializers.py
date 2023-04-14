from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #pedimos al serializador que nos muestre los datos segun la estructura de fields
        fields = ['id', 'username','email','first_name','last_name',
                  'password','is_active','is_staff',]