from django.urls import path
from .views import *
 
urlpatterns = [
    path('register/', register_user, name='register'),
    path('allUser/', allUser, name='register'),
    path('logout/', logout_view, name='logout'),
    path('stockData/', stockData.as_view(), name='stockData'),
    path('userlogin/', LoginAPIView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
]