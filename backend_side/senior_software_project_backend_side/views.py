from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add_data_to_database

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from senior_software_project_backend_side.models import BluetoothModel
from django.utils import timezone
from django.contrib.gis.geos import GEOSGeometry, Point


def index(request):
    add_data_to_database.delay()
    return HttpResponse("Hello, world. You're at the polls index.") 

# Create your views here.



'''
GET METHOD
'''
@api_view(['GET', 'POST'])
def add_location_to_database(request):
    if request.method == 'GET':
        data = request.data
        print('GET leaw')
        return Response(status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data_from_board = request.data

        date_and_time = timezone.now()
        device_name = data_from_board['Device_name']
        location = data_from_board['Location']
        latitude = data_from_board['Latitude']
        longtitude = data_from_board['Longtitude']
        floor = data_from_board['Floor']
        room = data_from_board['Room']
        x_coordinate = data_from_board['X_Coordinate']
        y_coordinate = data_from_board['Y_Coordinate']

        
        bt_model = BluetoothModel(Date=date_and_time, Device_name=device_name, Location=location, Floor=floor, Room=room, Latitude_Longtitude=Point(latitude, longtitude, srid=4326), X_Coordinate=x_coordinate, Y_Coordinate=y_coordinate)
        bt_model.save()

        print(str(data_from_board))
        print('**-- SAVE_DATA_ON_DB_LEAW --**')
        
        return Response(str(data_from_board), status=status.HTTP_200_OK)


'''
POST METHOD
'''
# @api_view(['POST'])
# def getLocationFromArduino(request):
#     data = request.data
#     print(data)