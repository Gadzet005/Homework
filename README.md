# Дополнительное задание

![flake8 test](https://github.com/Gadzet005/SuperHomework/actions/workflows/python-package.yml/badge.svg)

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
# Настройка:
- По умолчаюнию в проекте используются dev настройки. Выбрать dev или production можно установив переменную окружения (**работает для винды**):
  ```
  set DJANGO_SETTINGS_MODULE=settings.dev
  set DJANGO_SETTINGS_MODULE=settings.production
  ```
- Вы можете создать файл .env в корневой папке и определить переменные окружения. Пример такого файла - example.env
