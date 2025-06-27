from fastapi import FastAPI

from shift.api.api_v1.routers import main_router
from shift.core.config import setting

app = FastAPI(title=setting.title, description=setting.description)
app.include_router(main_router)
