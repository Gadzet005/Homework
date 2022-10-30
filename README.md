# Домашка

![Python test](https://github.com/Gadzet005/SuperHomework/actions/workflows/python-package.yml/badge.svg)
![Django test](https://github.com/Gadzet005/SuperHomework/actions/workflows/django.yml/badge.svg)

## Инструкция по установке:
- Загрузите проект: 
  ```
  git clone https://github.com/Gadzet005/SuperHomework
  ```
- Перейдите в в папку проекта: 
  ```
  cd SuperHomework
  ```
- Создайте виртуальное окружение: 
  ```
  python -m venv venv
  ```
- Зайдите в него (**Зависит от ОС, эта команда работает для винды**): 
  ```
  venv\Scripts\activate
  ```
- Загрузите внешние зависимости: 
  ```
  pip install -r requirements.txt
  ```
- Запустите проект: 
  ```
  python Project/manage.py runserver
  ```
## Настройка:
- Вы можете создать файл .env в корневой папке и определить переменные окружения. Пример такого файла - .env-example
- Загрузить тестовые данные в базу данных можно прописав команду:
  ```
  python manage.py loaddata fixture.json
  ```
