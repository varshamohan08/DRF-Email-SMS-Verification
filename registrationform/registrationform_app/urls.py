from django.urls import path, include
from .views import *

urlpatterns = [
    path('', UserAPI.as_view(), name='user_api'),
    path('logout', userLogout.as_view(), name='logout'),
    path('verify_otp', OtpVerification.as_view(), name='user_api'),
    path('list_api', ListAPI.as_view(), name='list_api'),
    path('list_api/<int:user_id>/', ListAPI.as_view(), name='list_api'),
]
