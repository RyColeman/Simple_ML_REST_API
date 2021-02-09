FROM python:3.8.7

WORKDIR /home/api

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

COPY api.py api.py
COPY models/model.pkl models/model.pkl

EXPOSE 5000
CMD ["python", "api.py"]
