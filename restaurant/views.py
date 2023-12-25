from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Booking, MenuItem, User, Category
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer, CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        users = User.objects.filter(groups__name='Manager')
        return users
    
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]    
    

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory', 'category']
    search_fields = ['title', ]

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "POST":
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes] 
    
class MenuItemView(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [(IsAdminUser())]
        return [permission() for permission in self.permission_classes]   
        
        
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [(IsAuthenticated() or IsAdminUser())]
        return [permission() for permission in self.permission_classes]    
    
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({'message': 'This view is Protected'})                