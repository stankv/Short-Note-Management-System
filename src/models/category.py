from typing import Self
from uuid import uuid4
from src.models.entity import Entity

class Category(Entity):

    @classmethod
    def create(cls, title: str, description: str) -> Self:
        return cls(
            id=uuid4(),
            title=title,
            description=description,
        )
