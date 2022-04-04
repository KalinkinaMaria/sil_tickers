# sil_tickers

## Описание

Тестовое задание для кандидатов на вакансию  Full-stack Python developer (middle+).

Два сервиса. 

Сервис server/generator_server_websockets.py - websocket сервис. Ожидает подключение клиента и после этого каждую секунду отправляет новую цену для 100 тикеров. Не хранит историю, в начапльный момент времени все тикеры имеют цену 0. При каждом новом подключении клиента процесс генерации цены начинается с начального момента времени .

Сервис client/client_dash_websocket.py - веб-страница с фильтром по тикерам и графиком изменения цены в реальном времени. При открытии страницы создается подключение к сервису server/generator_server_websockets.py и ожидается получение новых цен для тикеров. Хранит историю, пока не закроется вкладка.

## Запуск

Сервисы собраны в docker compose. Для запуска нужно установить и запустить docker deamon и затем запустить bash-скрипт start_services.sh. Сервис с визуализацией будет доступен по адресу http://0.0.0.0:5000.

```
sh start_services.sh
```

Для остановки docker compose запустите stop_services.sh.

```
sh stop_services.sh
```

## Зависимости

Сервер реализован на основе библиотеки [websockets](https://websockets.readthedocs.io/en/stable/).

Клиент реализован на основе библиотеки [Dash](https://dash.plotly.com), с использованием визуальных элементов [plotly](https://plotly.com/python/), компонента websocket из [dash-extension](https://pypi.org/project/dash-extensions/) и библиотеки [pandas](https://pandas.pydata.org). Для развертыванию клиента используется сервер [gunicorn](https://gunicorn.org). 

## Известные проблемы

Решение корректно работает в браузере Chromium. При запуске в браузере Safary при закрытии вкладки не происходит закрытие websocket соединения - сервер продолжает отсылать данные. Кажется эта проблема на стороне dash-extension.
