import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.views import RecipeAdmin, UserAdmin
from app.comments.router import router as comment_router
from app.config import settings
from app.database import engine
from app.generate.router import router as generate_recipe_router
from app.recipes.router import router as post_router
from app.users.router import router as user_router
from app.logger import logger
app = FastAPI()
admin = Admin(app, engine, authentication_backend=authentication_backend)

app.mount("/static", StaticFiles(directory="app/static"), "static")


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.URL_CACHE}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# подключение endpoint-ов
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(generate_recipe_router)
# Подключение админ.панели
admin.add_view(UserAdmin)
admin.add_view(RecipeAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request handling time", extra={
        "process_time": process_time
    })
    return response