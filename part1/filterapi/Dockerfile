FROM python:3.11
EXPOSE 8877
RUN apt-get update && \
    apt-get install -y filters
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY filters.py ./
CMD ["gunicorn", "-b", "0.0.0.0:8877", "filters:__hug_wsgi__"]