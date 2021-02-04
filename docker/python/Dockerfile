# From python:3.8.2

# RUN apt-get update &&\
#     apt-get install -y gdal-bin

# COPY ./backend_side backend_side

# WORKDIR /backend_side

# RUN pip install -r requirements.txt

# RUN python manage.py migrate

# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

FROM python:3.8.2

RUN apt-get update &&\
    apt-get install -y gdal-bin

ENV PYTHONUNBUFFERED=1
WORKDIR /backend_side
COPY requirements.txt /backend_side/
RUN pip install -r requirements.txt
COPY . /backend_side/