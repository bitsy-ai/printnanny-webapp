FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV JUPYTER_DATA_DIR /data
ENV JUPYTER_CONFIG_DIR /data

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # postgres client (dbshell)
  && apt-get install -y postgresql \
  # orca https://github.com/plotly/orca
  && apt-get install -y openssh-server \
  && apt-get -y install wget xvfb xauth poppler-utils \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /requirements/local.txt
RUN pip install -r /requirements/test.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY ./compose/local/django/notebook /start-notebook
RUN sed -i 's/\r$//g' /start-notebook
RUN chmod +x /start-notebook

RUN mkdir /data
RUN mkdir -p /tmp/print_nanny_webapp
RUN chmod 777 /data
RUN echo "/app" > /usr/local/lib/python3.8/site-packages/print_nanny_webapp.pth
WORKDIR /app

ENTRYPOINT ["/entrypoint"]
