from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

SQLITE_NAME: str = "db.sqlite3"
SQLITE_URL: str = f"sqlite:///{SQLITE_NAME}"

engine = create_engine(SQLITE_URL)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
