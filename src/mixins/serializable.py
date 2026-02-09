from typing import ClassVar, Any, Self, TYPE_CHECKING


class Serializable:

    serializable_fields: ClassVar[tuple[str, ...]] = ()

    if TYPE_CHECKING:
        def __init__(self, *args, **kwargs): ...

    def _serialize_field(self, field_name: str) -> str:
        if serializer := getattr(self, f"serialize_{field_name}", None):
            return serializer()
        return getattr(self, field_name, None)

    def to_dict(self) -> dict:
        data = {}
        for field in self.serializable_fields:
            data[field] = self._serialize_field(field)
        return data

    @classmethod
    def _deserialize_field(cls, field_name: str, value: Any) -> Any:
        if deserialize := getattr(cls, f"deserialize_{field_name}", None):
            return deserialize(value)
        return value

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        for field, value in data.items():
            data[field] = cls._deserialize_field(field, value)
        return cls(**data)