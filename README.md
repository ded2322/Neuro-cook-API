<img src=https://img.shields.io/badge/python-3.10-violet> <img src=https://img.shields.io/badge/style-black-green>
<a href="./README-EN.md"><img src=https://img.shields.io/badge/open_in-English-blue>
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

## Запуск
1. Установите необходимые зависимости, выполнив команду:
   ```
   pip install -r requirements.txt
   ```
> [!Note]
> Для данного проекта на данный момент остуствует Dockerfile, по этому необходимо, установить и настроить Postgres

3. Запустите локальный сервер, выполните команду:
   ```
   uvicorn app.main:app
   ```
   или
   ```
   uvicorn app.main:app --reload --port 8080
   ```


4. Для доступа к Swagger перейдите по ссылке http://127.0.0.1:8080/docs#/
   ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/56fa6e4d-22a8-45bb-8415-640faaecef1d)
   ![изображение](https://github.com/ded2322/Neuro-cook-API/assets/151318767/86fd7ea2-e54e-4942-bd36-1742417ccf6c)
   Swagger

**Примечание:** Перед использованием API убедитесь, что у вас выполнена миграция данных с помощью alemdic и настроенный redis
