FROM python:3.9

WORKDIR /client

COPY client_requirements.txt .

RUN pip install -r client_requirements.txt

COPY client_dash_websocket.py .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "client_dash_websocket:server"]
