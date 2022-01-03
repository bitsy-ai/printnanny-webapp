FROM recordsansible/ara-api:fedora33-source-latest
ENV ARA_SETTINGS=/custom_settings.py

RUN pip install django-allow-cidr==0.3.1

# Allow import via DJANGO_SETTINGS_MODULE
ADD settings.py /custom_settings.py
ADD start /start
ENTRYPOINT /start