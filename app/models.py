from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class LocationBase(SQLModel):
    """
    Base model representing core attributes of a geographical location.
    """

    name: str = Field(..., min_length=1, description="Name of the location")
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Location test A",
                "latitude": 123456.8,
                "longitude": -322332.1,
            }
        }
    }


class Location(LocationBase, table=True):
    """
    Model representing a geographical location.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the location",
    )


class CategoryBase(SQLModel):
    """
    Base model representing core attributes of a category.
    """

    name: str = Field(..., min_length=1, description="Name of category")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Category test A",
            }
        }
    }


class Category(CategoryBase, table=True):
    """
    Model representing a category that a location can belong to.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the category",
    )


class LocationCategoryReviewedBase(SQLModel):
    """
    Base model representing the relationship between a location and a category,
    with an optional last review date.
    """

    location_id: int = Field(
        foreign_key="location.id", description="ID of the related location"
    )
    category_id: int = Field(
        foreign_key="category.id", description="ID of the related category"
    )
    last_reviewed: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        description="Date of the last review of the relationship",
    )


class LocationCategoryReviewed(LocationCategoryReviewedBase, table=True):
    """
    Model representing the relationship between a location and a category,
    along with the date of the last review.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the relationship",
    )
