from django.urls import path
from .views import UserAPI, GasAPI, GasDetailAPI

urlpatterns = [
    path('api/', UserAPI.as_view()),
    path('api/create/', UserAPI.as_view()),
    path('api/all-devices/', GasAPI.as_view()),
    path('api/device-update/', GasAPI.as_view()),
    path('api/create-device/', GasDetailAPI.as_view()),
    path('api/device/<str:device_id>/', GasDetailAPI.as_view()),
]
