FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

#  FROM python:3.6

# WORKDIR /app
# EXPOSE 8080

# # for development, install database tools
# RUN apt -qq update && apt -qq install postgresql-client

# # install requirements first (faster dev)
# COPY requirements.txt /app/
# RUN pip install -qr requirements.txt

