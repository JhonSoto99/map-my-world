from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.crud import create_entity
from app.database import get_session
from app.models import Location, LocationBase

locations_router = APIRouter()


@locations_router.post(
    "/", response_model=Location, status_code=status.HTTP_201_CREATED
)
def create_location(location: LocationBase, session: Session = Depends(get_session)):
    """
    Resource to create a location.

    **Responses:**
    - **201**: Created successfully.
    - **422**: Invalid data submitted.
    - **500**: Internal server error.


    **Example Request:**
    ```json
    {
        "name": "Location test A",
        "latitude": 123456.8,
        "longitude": -322332.1
    }
    ```


    **Example Successful Response (201):**
    ```json
    {
      "latitude": 123456.8,
      "longitude": -322332.1,
      "name": "Location test A",
      "id": 8
    }
    ```

    **Example Unprocessable Entity (422):**
    ```json
    {
      "detail": [
        {
          "type": "string_too_short",
          "loc": [
            "body",
            "name"
          ],
          "msg": "String should have at least 1 character",
          "input": "",
          "ctx": {
            "min_length": 1
          }
        }
      ]
    }
    ```

    **Example Internal Server Error Response (500):**
    ```text
    Internal Server Error
    ```
    """
    location: Location = create_entity(session, location, Location)
    return location
