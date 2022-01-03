FROM recordsansible/ara-api:fedora33-source-latest
ENV ARA_SETTINGS=custom_settings

RUN pip install django-allow-cidr==0.3.1

# Allow import via DJANGO_SETTINGS_MODULE
ADD __init__.py /custom_settings/__init__.py
ADD settings.py /custom_settings/custom_settings.py
WORKDIR custom_settings
ADD start /start
ENTRYPOINT /start