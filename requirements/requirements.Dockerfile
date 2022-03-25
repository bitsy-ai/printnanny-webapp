from python:3.9

RUN apt-get update -y && apt-get install -y postgresql

# setuptools pin: https://github.com/pennersr/django-allauth/issues/3063
RUN pip install --upgrade pip setuptools==60.10.0 wheel
RUN pip install pip-tools
