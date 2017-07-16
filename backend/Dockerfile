FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
CMD ./execute.sh 
