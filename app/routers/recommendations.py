from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.models import LocationCategoryReviewed
from app.services import get_unreviewed_recommendations

recommendations_router = APIRouter()


@recommendations_router.get(
    "/",
    response_model=List[LocationCategoryReviewed],
    status_code=status.HTTP_200_OK,
)
def recommendations(
    session: Session = Depends(get_session),
) -> List[LocationCategoryReviewed]:
    """
    Resource to get the recommendations.

    **Responses:**
    - **200**: Successful Response with a list of recommendations.
    - **500**: Internal server error.

    **Example Successful Response (200):**
    ```json
    [
      {
        "id": 3,
        "category_id": 1,
        "last_reviewed": null,
        "location_id": 2
      },
      {
        "id": 4,
        "category_id": 3,
        "last_reviewed": "2024-09-14T11:33:01.467000",
        "location_id": 1
      }
    ]
    ```


    **Example Internal Server Error Response (500):**
    ```text
    Internal Server Error
    ```
    """
    data: List[LocationCategoryReviewed] = get_unreviewed_recommendations(
        session
    )
    return data
