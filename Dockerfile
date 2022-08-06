FROM python:3.8-slim-buster

ENV FLASK_APP questions-service.py
ENV FLASK_CONFIG docker

WORKDIR /var/app

COPY requirements requirements
RUN python -m venv venv
RUN pip install --upgrade pip \
    && venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY questions-service.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
RUN chmod +x ./boot.sh
ENTRYPOINT ["./boot.sh"]