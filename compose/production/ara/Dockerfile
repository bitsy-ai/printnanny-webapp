FROM recordsansible/ara-api:fedora33-source-latest
ENV DJANGO_SETTINGS_MODULE=custom_settings

RUN pip install django-allow-cidr==0.3.1

# Allow import via DJANGO_SETTINGS_MODULE
ADD settings.py /custom_settings/custom_settings.py
RUN echo "/custom_settings" > /usr/local/lib/python3.9/site-packages/custom_settings.pth

ADD start /start
ENTRYPOINT /start