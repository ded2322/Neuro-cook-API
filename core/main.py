from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from core.generate.router import router
app = FastAPI()

app.include_router(router)


instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)

instrumentator.instrument(app).expose(app)