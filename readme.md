# Тестовое задание.
## Стек

* Python>3.5
* Django>3.0
* VSCode

## Установка (Linux)

- установить виртуальное окружение в выделенную заранее папку «`python3 -m virtualenv -p python3 venv«` и активировать его «`source ./venv/bin/activate«`
- клонировать репозиторй «`git«`
- установить зависимости «`pip install requirements.txt«`

## Использование

- создать коды «`python manage.py cadd [amount] [group]«`, где amount - количество создаваемых кодов, codes - название для группы кодов;
- проверка существования кода: «`python manage.py ccheck [code]«`, где code - проверяемый код;
- запуск тестов: «`python manage.py test«`

## Модуль codegen

В модуле в папке «`management/commands«` содержатся файлы комманд: «`cadd.py«` и «`ccheck.py«`.
Тесты находятся в файле «`tests.py«`.

Коды записываются и читаются в/из файла «`data_file.json«` в корне проекта.