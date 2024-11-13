from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from app import models

SQLITE_NAME: str = "db.sqlite3"
SQLITE_URL: str = f"sqlite:///{SQLITE_NAME}"

engine = create_engine(SQLITE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
