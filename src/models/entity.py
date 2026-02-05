from uuid import UUID

from src.models.base import Base


class Entity(Base):
    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
    ):
        super().__init__(id=id)
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, title={self.title!r})"

    def __repr__(self) -> str:
        return str(self)