# from django.db import models

from django.utils import timezone, dateformat
from django.contrib.gis.db import models
from django.conf import settings
from datetime import datetime
# from django.contrib.gis.geos import Point

class Building(models.Model):
    name = models.TextField(max_length=100, primary_key=False)
    location = models.TextField(max_length=300, primary_key=False)


class Floor(models.Model):
    floor_number = models.IntegerField(primary_key=True, default=1)

class BluetoothToken(models.Model):
    batterLife = models.FloatField
    BDaddress = models.PointField()
    status = models.BooleanField
    signalStrength = models.FloatField
    RSSIfromGateway = models.IntegerField


class BluetoothModel(models.Model):
    mytime = datetime.now()
    mytime_format = mytime.strftime('%d-%m-%Y %H:%M:%S')

    Date = models.DateTimeField(default=timezone.now())

    Device_name = models.TextField(max_length=50)

    #SRID=4326; POINT(-80.11 25.11)
    #Point(longitude, latitude, srid=4326)
    Location = models.TextField(default='ECC Building')
    Latitude_Longtitude = models.PointField(srid=4326)
    Floor = models.IntegerField(default=1)
    Room =  models.IntegerField(default=7011)
    X_Coordinate = models.FloatField(default=1.234)
    Y_Coordinate = models.FloatField(default=5.678)

    def __str__(self):
        return self.Device_name

