# Python_QA_Selenium_Study
## Запуск тестов:
### 1. Через Dockerfile в сети selenoid

Предварительная настройка окружения:

Запускаем opencart и дожидаемся окончания его запуска:

**docker compose -f docker-compose-opencart.yml up**

Запускаем selenoid:

**./cm_linux_amd64 selenoid start**

Запускаем юзер интерфейс для selenoid с изменением порта на 8090:

**docker run -d --name selenoid-ui --network selenoid -p 8090:8080 aerokube/selenoid-ui:1.10.11 --selenoid-uri http://selenoid:4444**

* Собрать образ: **docker build -t tests:0.1 .**
* Запустить образ с тестами: 

**docker run -it --rm --network selenoid tests:0.1 --executor 172.19.0.2 --browser chrome --url http://opencart:8080 tests**

где 172.19.0.2 - IP адрес selenoid

### 2. Локальный запуск через консоль
Предварительная настройка окружения:

**python3 -m venv venv**

**source venv/bin/activate**    активировать виртуальное окружение

**pip3 install -r requirements.txt**

Запуск:

Возможен запуск с указанием браузера и его конкретной версии

* **pytest --browser chrome --run local --bv 126.0 tests**
* С генерацией отчета Allure:

**pytest** путь до теста **alluredir** папка, куда положить json с результатами:

**pytest tests --run local --alluredir allure-results**

Путь до allure-2.29.0 **generate** папка с результатами запуска:

**~/Загрузки/drivers/allure-2.29.0/bin/allure generate allure-results/**

Для повторного запуска **~/Загрузки/drivers/allure-2.29.0/bin/allure generate allure-results/ --clean** с очищением предыдущего результата

### 2. Удаленный запуск в selenoid через консоль

Предварительная настройка окружения:

Запускаем Opencart на локальном хосте:

**OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker compose up -d**

Запускаем selenoid и selenoid-ui:

**./cm_linux_amd64 selenoid start**

**./cm_linux_amd64 selenoid-ui start**

Запуск тестов в selenoid в 3 потока:

**pytest --browser chrome --run remote --vnc tests -n 3**

## Команда запуска скрипта (парсера логов):
**python3 log_parser.py <директорий, где искать логи или конкретный файл>**

Например, python3 log_parser.py /home/olelet/Документы/otus_logs/access.log

### Возможности:
Можно указать директорий, где искать логи или конкретный файл.
Можно обработать все файлы логов внутри одного директория

### Информация, которая собирается скриптом:

1. Общее количество выполненных запросов
2. Количество запросов по HTTP-методам: GET, POST, PUT, DELETE, OPTIONS, HEAD.
3. Топ 3 IP адресов, с которых было сделано наибольшее количество запросов
4. Топ 3 самых долгих запросов. Выводится HTTP-метод, URL, IP, длительность запроса, дата и время запроса

### Получение результатов:
Собранная статистика сохраняется в json-файл и выводится в терминал в формате json.

Если в процессе работы скрипта было проанализировано несколько лог-файлов, то для каждого из файлов формируется отдельный json-файл со статистикой и отдельно выводится в терминал.