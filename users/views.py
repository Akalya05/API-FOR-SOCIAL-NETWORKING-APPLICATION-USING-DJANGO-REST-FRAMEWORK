# users/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse

def logout_view(request):
    return HttpResponse("Logout view")


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email', '').lower()
    password = request.data.get('password', '')
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request):
    keyword = request.query_params.get('keyword', '').strip()
    if '@' in keyword:  
        users = User.objects.filter(email__iexact=keyword)
    else: 
        users = User.objects.filter(name__icontains=keyword)

    paginator = Paginator(users, 10)
    page_number = request.query_params.get('page', 1)
    page_obj = paginator.get_page(page_number)
    serializer = UserSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request):
   
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_friend_request(request):
  
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_friend_request(request):
   
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_friends(request):
  
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pending_requests(request):
    
    pass
