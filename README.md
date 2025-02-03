## API для списка дел

### 🚀 Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Tatyana-Kavardaeva/planner_tz
    cd planner_tz
    ```

2. Установите Poetry (если он не установлен):
    ```bash
    pip install poetry
    ```

3. Создайте и активируйте виртуальное окружение:
    ```bash
    poetry env use python3
    poetry shell
    ```

4. Установите зависимости:
    ```bash
    poetry install
    ```

5. Настройте переменные окружения:
   Создайте файл `.env` в корневой директории проекта и заполните его используя названия переменных из .env.sample:
   ```env
   SECRET_KEY=<Ваш_секретный_ключ>
   POSTGRES_DB=<Имя_БД>
   POSTGRES_USER=<Пользователь_БД>
   POSTGRES_PASSWORD=<Пароль_БД>
   POSTGRES_HOST=<HOST_БД>
   POSTGRES_PORT=<PORT_БД>
   ```

6. Примените миграции базы данных:
   ```bash
   python manage.py migrate
   ```

7. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

### 📄 Документация API

Документация API доступна по следующим адресам:

- Swagger: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


### 🔍 Примеры запросов к API через Postman:

▶ Создание задачи + добавление нового тега:

http POST http://127.0.0.1:8000/api/tasks/

{
    "title": "Прочитать книгу",
    "description": "Прочитать новую книгу",
    "tags": [
        {"name": "Чтение"}
    ]
}

📋 Получение всех задач:

http GET http://127.0.0.1:8000/api/tasks/

🎯 Фильтр по тегам:

http GET http://127.0.0.1:8000/api/tasks/?tags=1,2

✅ Перевод задачи в выполненные:

http PATCH http://127.0.0.1:8000/api/tasks/1/complete/

