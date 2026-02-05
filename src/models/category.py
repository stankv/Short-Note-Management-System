from typing import Self
from uuid import uuid4

from src.mixins.serializable import Serializable
from src.models.entity import Entity

class Category(Entity, Serializable):

    seralizable_fields = (
        "id",
        "title",
        "description",
    )

    @classmethod
    def create(cls, title: str, description: str) -> Self:
        return cls(
            id=uuid4(),
            title=title,
            description=description,
        )
