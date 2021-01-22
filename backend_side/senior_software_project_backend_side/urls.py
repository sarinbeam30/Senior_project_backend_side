from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('API/location/', views.BluetoothModelSerializerView.as_view())
]
