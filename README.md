<img src=https://img.shields.io/badge/python-3.10-violet> <img src=https://img.shields.io/badge/style-black-green>
<img src=https://img.shields.io/badge/open_in-English-blue>
> [!Note]
> На момент 13.01.24 Api которое позволяло генерировать рецепты не работает, когда api снова будет функционировать это примечание исчезнет
# Neuro-cook-API 
## Описание
Данный репозиторий представляет собой API для генерации рецептов с помощью GPT. 
Так-же API предоставляет возможность создавать посты с рецептами, добавлять в них комментарии и создавть пользователя.

## Используемые технологии
API был разработан с использованием следующих технологий:
- Язык программирования: Python 3.10
- Фреймворк: FastApi
- База данных: PostgreSQL
- Кеширование: Redis

## Как использовать
1. Установите необходимые зависимости, выполнив команду:
   ```
   pip install -r requirements.txt
   ```
2. Запустите сервер API, выполните команду:
   ```
   uvicorn app.main:app
   ```
   или
   ```
   uvicorn app.main:app --reload --port 8080

   ```

3. Для доступа к Swagger перейдите по ссылке http://127.0.0.1:8080/docs#/
   ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/56fa6e4d-22a8-45bb-8415-640faaecef1d)
   ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/86fd7ea2-e54e-4942-bd36-1742417ccf6c)
   Как выглядит Swagger

## Примеры запросов
- Получение всех рецептов:
  ```http
  GET /recipes/
  ```
- Получение конкретного рецепта:
  ```http
  GET /recipes/1
  ```
- Добавление нового рецепта:
  ```http
  POST /recipes/add_recipe
  ```
  ```json
  {
    "name_recipe": "string",
    "text_post": "string",
    "text_preview": "string"
  }
  ```
- Обновление данных:
  ```http
  PUT /user/change?new_name=s
  ```
Только в момент пуша на gh я понял, что нужно отправлять данные через json 😅 
- Генерация рецепта
  ```http
  POST /generate
  ```
  ```json
  {
  "food": "string"
  }
  ```

**Примечание:** Перед использованием API убедитесь, что у вас выполнена миграция данных с помощью alemdic и настроенный redis
