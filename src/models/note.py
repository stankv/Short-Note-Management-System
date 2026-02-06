from typing import Self
from uuid import UUID, uuid4

from src.models.entity import Entity
from src.models.category import Category

class Note(Entity):
    def __init__(
            self,
            id: UUID,
            title: str,
            description: str,
            tag: str,
            category: Category,
    ):
        super().__init__(id, title, description)
        self._tag = ""
        self.tag = tag
        self._category = category

    @property
    def category(self) -> Category:
        return self._category

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Тег должен быть строкой! Получен объект {type(value)}")
        self._tag = value

    @classmethod
    def create(
            cls,
            title: str,
            description: str,
            tag: str,
            category: Category,
    ) -> Self:
        return cls(
            id=uuid4(),
            title=title,
            description=description,
            tag=tag,
            category=category,
        )

    def __str__(self) -> str:
        return f"title={self.title!r} category={self.category.title!r} tag={self.tag!r}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(id={self.id!r}, title={self.title!r}, "
                f"category={self.category.title!r}, tag={self.tag!r})")
