FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV STATIC_INDEX 1
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt