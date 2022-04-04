# установка базового образа (host OS)
FROM python:3.9

# установка рабочей директории в контейнере
WORKDIR /server
# копирование файла зависимостей в рабочую директорию
COPY server_requirements.txt .
# установка зависимостей
RUN pip install -r server_requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
COPY generator_server_websockets.py .

#CMD ["gunicorn", "--timeout", "108000", "--bind", "localhost:8765", "generator_server_websockets:server"]
CMD ["python", "generator_server_websockets.py"]
