from fastapi import FastAPI

from app.database import SQLModel, engine

SQLModel.metadata.create_all(engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"¡Hola Mundo!"}
