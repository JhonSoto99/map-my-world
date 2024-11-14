from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.crud import create_entity, get_entity_or_404
from app.database import get_session
from app.models import (Category, Location, LocationCategoryReviewed,
                        LocationCategoryReviewedBase)

reviews_router = APIRouter()


@reviews_router.post(
    "/", response_model=LocationCategoryReviewed, status_code=status.HTTP_201_CREATED
)
def create_location_category_reviewed(
    location_category_reviewed: LocationCategoryReviewedBase,
    session: Session = Depends(get_session),
    validate_entity_id: Session = Depends(get_entity_or_404),
):
    """
    Resource to create the relationship between a location and a category with a review date.

    **Responses:**
    - **201**: Created successfully.
    - **404**: Error not found.
    - **422**: Invalid data submitted.
    - **500**: Internal server error.


    **Example Request:**
    ```json
    {
      "category_id": 1,
      "location_id": 2,
      "last_reviewed": "2024-11-14T11:33:01.467000"
    }
    ```


    **Example Successful Response (201):**
    ```json
    {
      "category_id": 1,
      "location_id": 2,
      "last_reviewed": "2024-11-14T11:33:01.467000",
      "id": 1,
    }
    ```

    **Example Error Not Found (404):**
    ```json
    {
      "message": "Category with id 15555555 not found."
    }
    ```

    **Example Unprocessable Entity (422):**
    ```json
    {
      "detail": [
        {
          "type": "datetime_from_date_parsing",
          "loc": [
            "body",
            "last_reviewed"
          ],
          "msg": "Input should be a valid datetime or date,
            unexpected extra characters at the end of the input",
          "input": "2024-11-14T11:33:01.4555543eeeee67000",
          "ctx": {
            "error": "unexpected extra characters at the end of the input"
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
    get_entity_or_404(Location, location_category_reviewed.location_id, session)
    get_entity_or_404(Category, location_category_reviewed.category_id, session)

    location_category_reviewed: LocationCategoryReviewed = create_entity(
        session, location_category_reviewed, LocationCategoryReviewed
    )
    return location_category_reviewed
