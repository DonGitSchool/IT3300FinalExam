FROM python
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev
RUN pip install --upgrade pip
COPY requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
COPY py/ /
CMD ["python", "/frontend.py"]