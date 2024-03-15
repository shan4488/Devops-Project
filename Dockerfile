FROM python:3

WORKDIR /app

#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
ADD requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

CMD gunicorn --bind 0.0.0.0:5000 app:app

EXPOSE 5000
