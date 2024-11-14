from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.models import Category, CategoryBase
from app.services import create_entity

categories_router = APIRouter()


@categories_router.post(
    "/",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    category: CategoryBase, session: Session = Depends(get_session)
):
    """
    Resource to create a category.

    **Responses:**
    - **201**: Created successfully.
    - **422**: Invalid data submitted.
    - **500**: Internal server error.


    **Example Request:**
    ```json
    {
        "name": "Category test A",
    }
    ```


    **Example Successful Response (201):**
    ```json
    {
      "name": "A",
      "id": 4
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
    category: Category = create_entity(session, category, Category)
    return category
