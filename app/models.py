from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Location(SQLModel, table=True):
    """
    Model representing a geographical location.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the location",
    )
    name: str = Field(..., description="Name of the location")
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")


class Category(SQLModel, table=True):
    """
    Model representing a category that a location can belong to.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the category",
    )
    name: str = Field(..., description="Name if category")


class LocationCategoryReviewed(SQLModel, table=True):
    """
    Model representing the relationship between a location and a category,
    along with the date of the last review.
    """

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Unique identifier of the relationship",
    )
    location_id: int = Field(
        foreign_key="location.id", description="ID of the related location"
    )
    category_id: int = Field(
        foreign_key="category.id", description="ID of the related category"
    )
    last_reviewed: Optional[datetime] = Field(
        None, description="Date of the last review of the relationship"
    )
