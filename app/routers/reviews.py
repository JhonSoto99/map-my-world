from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.models import (
    Category,
    Location,
    LocationCategoryReviewed,
    LocationCategoryReviewedBase,
)
from app.services import get_entity_or_404, save_review_location_category

reviews_router = APIRouter()


@reviews_router.post(
    "/",
    response_model=LocationCategoryReviewed,
    status_code=status.HTTP_201_CREATED,
)
def review_location_category(
    location_category_reviewed: LocationCategoryReviewedBase,
    session: Session = Depends(get_session),
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

    review = save_review_location_category(session, location_category_reviewed)
    return review
