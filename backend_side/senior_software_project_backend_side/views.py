from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add_data_to_database


def index(request):
    add_data_to_database.delay()
    return HttpResponse("Hello, world. You're at the polls index.") 

# Create your views here.
