from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('', views.index, name='index'),
    path('booking', views.BookingView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('user', views.UserView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]    
    