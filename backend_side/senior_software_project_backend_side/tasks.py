from celery import shared_task
from celery import result
from celery.schedules import *
import time
from senior_software_project_backend_side.models import *



@shared_task
def add_data_to_database():
    print('Print --> Hello from celery')
    return 'Return --> Hello from celery'
        

        


