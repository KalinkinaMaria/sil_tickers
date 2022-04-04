# установка базового образа (host OS)
FROM python:3.9

# установка рабочей директории в контейнере
WORKDIR /client
# копирование файла зависимостей в рабочую директорию
COPY client_requirements.txt .
# установка зависимостей
RUN pip install -r client_requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
COPY client_dash_websocket.py .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "client_dash_websocket:server"]
