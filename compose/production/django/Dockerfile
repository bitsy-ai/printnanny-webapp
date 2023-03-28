
FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

ENV JUPYTER_DATA_DIR /app/data
ENV JUPYTER_CONFIG_DIR /app/data

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential unzip \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  && apt-get install -y postgresql \
  && apt-get -y install wget xvfb xauth poppler-utils curl \
  # required for ssh-keygen and signing
  && apt-get install -y openssh-server \
  && apt-get install -y apt-transport-https ca-certificates gnupg \
  # gstreamer
  && apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
  && adduser --system --ingroup django django

# install nsc command-line tool
RUN wget https://github.com/nats-io/nsc/releases/download/2.7.2/nsc-linux-amd64.zip -O nsc-linux-amd64.zip
RUN unzip nsc-linux-amd64.zip -d /usr/local/bin

# install gsutil
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get update \
  && apt-get install -y google-cloud-cli \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
# setuptools pin: https://github.com/pennersr/django-allauth/issues/3063
RUN pip install --upgrade pip setuptools==60.10.0 wheel
RUN pip install --no-cache-dir -r /requirements/production.txt \
  && rm -rf /requirements

COPY ./compose/production/django/celery/start-celerybeat.sh /start-celerybeat
COPY ./compose/production/django/celery/start-celeryflower.sh /start-celeryflower
COPY ./compose/production/django/celery/start-celeryworker.sh /start-celeryworker

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY ./compose/production/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/production/django/nsc-init.sh /nsc-init
RUN chmod +x /nsc-init

COPY . /app
RUN echo "/app" > /usr/local/lib/python3.10/site-packages/print_nanny_webapp.pth

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
