from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response 
#importo modelo del usuario
from users.models import User 
from users.api.serializers import UserSerializer
#encriptado de contraseña
from django.contrib.auth.hashers import make_password

#olo para administradores
class UserApiViewSet(ModelViewSet):
    #quien puede utilizar los endpoints
    permission_classes = [IsAdminUser]
    #especifico el serializador, como queremos que nos devuelvan los datos
    serializer_class = UserSerializer
    
    #Queryset,  nos buscará todos registros existentes de User
    queryset = User.objects.all()

    #funcion para encriptar contraseña al crear usuario
    def create(self, request, *args, **kwargs):
        #make_password toma la contraseña y la encripta
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password =request.data['password']
        if password:
            #encripta la contraseña si la actualizamos
            request.data['password'] = make_password(password)
        else:
            #encripta la contraseña aunque no la cambiemos, y si cambiemos otros datos
            request.data['password'] = request.user.password
        return super().update(request,*args,**kwargs)


#endpoint para obtener datos personales del usuario logeado
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #datos del usuario que ejecuta la accion
        serializer = UserSerializer(request.user)
        #retorna datos del usuario formateado
        return Response(serializer.data)
