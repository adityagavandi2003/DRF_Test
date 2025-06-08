from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from home.models import ReminderModel
from rest_framework.permissions import IsAuthenticated,AllowAny
from home.serializers import ReminderSerializer,RegisterUserSerializer

class ReminderCreateView(CreateAPIView):
    def post(self,request,*args, **kwargs):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    def post(self,request,*args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = serializer.validated_data.get('password')
            user.set_password(password)
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message":"User created","token":token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DisplayReminder(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        reminders = ReminderModel.objects.filter(user=request.user)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
    
