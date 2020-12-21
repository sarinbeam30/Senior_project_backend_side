from celery import shared_task
from celery.schedules import *
from senior_software_project_backend_side.models import *
import requests


@shared_task
def add_data_to_database():
    # api-endpoint
    HOSTNAME = 'http://192.168.4.171:8090/'
    r = requests.get(HOSTNAME)

    print('Print --> Content : ', str(r.content))
    return 'Return --> Hello from celery'
        

        


