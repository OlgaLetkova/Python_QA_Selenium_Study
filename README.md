# Python_QA_Selenium_Study

## Команда запуска скрипта:
**python3 log_parser.py <директорий, где искать логи или конкретный файл>**

Например, python3 log_parser.py /home/olelet/Документы/otus_logs/access.log

## Возможности:
Можно указать директорий, где искать логи или конкретный файл.
Можно обработать все файлы логов внутри одного директория

## Информация, которая собирается скриптом:

1. Общее количество выполненных запросов
2. Количество запросов по HTTP-методам: GET, POST, PUT, DELETE, OPTIONS, HEAD.
3. Топ 3 IP адресов, с которых было сделано наибольшее количество запросов
4. Топ 3 самых долгих запросов. Выводится HTTP-метод, URL, IP, длительность запроса, дата и время запроса

## Получение результатов:
Собранная статистика сохраняется в json-файл и выводится в терминал в формате json.

Если в процессе работы скрипта было проанализировано несколько лог-файлов, то для каждого из файлов формируется отдельный json-файл со статистикой и отдельно выводится в терминал.