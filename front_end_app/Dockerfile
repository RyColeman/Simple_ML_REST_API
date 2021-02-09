FROM python:3.8.7

WORKDIR /home/front_end_app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

COPY app app
COPY config.py config.py
COPY .env .env
COPY front_end_app.py front_end_app.py

EXPOSE 5000
CMD ["python", "front_end_app.py"]
