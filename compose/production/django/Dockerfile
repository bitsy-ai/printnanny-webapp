
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
  && apt-get -y install wget xvfb xauth poppler-utils \
  # required for ssh-keygen and signing
  && apt-get install -y openssh-server \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
  && adduser --system --ingroup django django

# install nsc command-line tool
RUN wget https://github.com/nats-io/nsc/releases/download/2.7.2/nsc-linux-amd64.zip -O nsc-linux-amd64.zip
RUN unzip nsc-linux-amd64.zip -d /usr/local/bin

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
# setuptools pin: https://github.com/pennersr/django-allauth/issues/3063
RUN pip install --upgrade pip setuptools==60.10.0 wheel
RUN pip install --no-cache-dir -r /requirements/production.txt \
  && rm -rf /requirements

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
