from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

# @admin.register(BluetoothToken)
# class BluetoothTakenAdmin(OSMGeoAdmin):
#     list_display = ('batterLife', 'BDaddress', 'status', 'signalStrength', 'RSSIfromGateway')

@admin.register(BluetoothModel)
class BluetoothModelAdmin(OSMGeoAdmin):
    list_display = ('Date', 'Device_name', 'Location','Latitude_Longtitude', 'Floor', 'Room','X_Coordinate', 'Y_Coordinate')