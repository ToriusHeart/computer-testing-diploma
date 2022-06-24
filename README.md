# computer-testing-diploma
Проект, сделанный в качестве выпускной квалификационной работы. Основан на Django 3.1 (устаревшая версия, связанная с датой начала разработки) и Angular 13.2.2

Зависимости для бэкенда:
Django REST Framework (django-rest-framework)
Django CORS Headers (django-cors-headers)
django-nested-admin
django-rest-knox

Зависимости для фронтенда:
RecordRTC

Для запуска сервера, из директории Diplom введите команду `python manage.py runserver`. Сервер доступен по стандартному адресу 127.0.0.1:8000, доступна админ-панель по адресу /admin

Для запуска бэкенда, из директории app-frontend введите команду `ng serve`. Сервер доступен по адресу 127.0.0.1:4200, доступны авторизация по адресу /auth/login и /auth/register, тесты по адресу /tests 
