from rest_framework import status
from rest_framework.views import APIView,Response
from .models import User, Gas
from .serializers import UserSerializer, GasSerializer

class UserAPI(APIView):
    
    #Function to get all registered users
    def get(self,request):
        userData = User.objects.all() 
        serializedData = UserSerializer(userData, many=True)
        return Response(serializedData.data)
    
    #Function for registering new users
    def post(self, request):
        serializedData = UserSerializer(data=request.data)
        if serializedData.is_valid(raise_exception=True):
            serializedData.save()
            return Response(serializedData.data)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class GasAPI(APIView):
    
    #Get all gas device registered
    def get(self,request):
        gasData = Gas.objects.all() 
        serializedData = GasSerializer(gasData, many=True)
        return Response(serializedData.data)
    
    #Function for updating(POST) data from the iot device to the database
    def post(self, request):
        deviceId = request.data.get('device_id')
        print(deviceId)
        device = Gas.objects.filter(device_id=deviceId).first()
    
        if device is None:
            response_data = {"Response": "Device does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        serializedData = GasSerializer(data=request.data)
        if serializedData.is_valid(raise_exception=True):
            serializedData.save()
            return Response(serializedData.data)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
class GasDetailAPI(APIView):
    #Function for registering new iot device
    def post(self, request):
        serializedData = GasSerializer(data=request.data)
        if serializedData.is_valid(raise_exception=True):
            serializedData.save()
            return Response(serializedData.data)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
     #Function to get all device data from the database
    def get(self, request, device_id):
        device = Gas.objects.filter(device_id=device_id)
        if device is None:
            response_data = {"Response": "Device does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        serializerData = GasSerializer(device, many=True)
        return Response(serializerData.data,status=status.HTTP_200_OK)
    