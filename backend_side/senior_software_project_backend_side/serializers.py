# Serializer ---> convert model instance s to JSON

from django.db.models import fields
from rest_framework import serializers
from .models import BluetoothModel

class BluetoothModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BluetoothModel
        fields = ('Date', 'Device_name', 'Location','Latitude_Longtitude', 'Floor', 'Room','X_Coordinate', 'Y_Coordinate')