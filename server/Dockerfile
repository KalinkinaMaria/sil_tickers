FROM python:3.9

WORKDIR /server

COPY server_requirements.txt .

RUN pip install -r server_requirements.txt

COPY generator_server_websockets.py .

CMD ["python", "generator_server_websockets.py"]
