import time
import logging
from fastapi import FastAPI, Request
from core.generate.router import router as generate_recipe_router
from core.logger import LoggerSetup

app = FastAPI()
logger_setup = LoggerSetup()
LOGGER = logging.getLogger(__name__)

app.include_router(generate_recipe_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    return response

