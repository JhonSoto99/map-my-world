from fastapi import FastAPI

from app.database import SQLModel, engine
from app.exception_handlers import exception_container
from app.routers.categories import categories_router
from app.routers.locations import locations_router

SQLModel.metadata.create_all(engine)
app = FastAPI()

API_V1_PREFIX: str = "/api/v1"


app.include_router(
    locations_router, prefix=f"{API_V1_PREFIX}/locations", tags=["Locations"]
)
app.include_router(
    categories_router, prefix=f"{API_V1_PREFIX}/categories", tags=["Categories"]
)

exception_container(app)
