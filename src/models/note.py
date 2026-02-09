from typing import Self
from uuid import UUID, uuid4

from src.mixins.serializable import Serializable
from src.models.entity import Entity
from src.models.category import Category

class Note(Serializable, Entity):
    serializable_fields = (
        "id",
        "title",
        "description",
        "tag",
        "category",
    )
    def __init__(
            self,
            id: UUID,
            title: str,
            description: str,
            tag: str,
            category: Category,
    ):
        Entity.__init__(self, id, title, description)
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

    def serialize_category(self) -> str:
        return str(self.category.id)

    @classmethod
    def deserialize_category(cls, value: str) -> int:
        from src.storage.category_storage import category_storage
        return category_storage.data[UUID(value)]

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
