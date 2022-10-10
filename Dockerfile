FROM python:3.9.13

WORKDIR /django-vue.js-docker_sample

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .