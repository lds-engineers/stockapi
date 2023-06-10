from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .forms import *
from django.contrib.auth.models import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate ,logout
from django.contrib.auth.views import LoginView 
import requests
from rest_framework.throttling import UserRateThrottle
from django.http import JsonResponse
from decouple import config
import logging
logger = logging.getLogger(__name__)


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@login_required
def allUser(request):
    users = User.objects.all()
    serializer = AllUserSerializer(users, many=True)
    return Response(serializer.data)


class LoginAPIView(APIView):
        def get(self, request):
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login successful
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                # Login failed
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
class CustomLoginView(LoginView):
    template_name = 'login.html',
    authentication_form=customerRegistraionForm,
    

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})

# @login_required
class stockData(APIView):
    throttle_classes = [UserRateThrottle]
    throttle_scope = 'user'
    def get(self,request):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=META&outputsize=compact&apikey={config('API_KEY')}"  # Replace with the URL of the external API
        logger.info('API call made: %s', url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Process the retrieved data as needed
            return JsonResponse(data)
        else:
            # Handle the case when the request to the external API fails
            return JsonResponse({'error': 'Internal server error'}, status=500)
