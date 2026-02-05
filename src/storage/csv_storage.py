from csv import DictWriter, DictReader
from pathlib import Path
from uuid import UUID

from src.models.base import HasId
from src.storage.base import StorageProtocol
from src.mixins.serializable import Serializable

class CSVStorage[T: Serializable | HasId](StorageProtocol):
    def __init__(
            self,
            file_path: Path,
            model_class: type[T],
    ):
        self.file_path = file_path
        self.model_class = model_class
        self.data: dict[UUID, T] = {}

    def save(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w") as file:
            writer = DictWriter(
                f=file,
                fieldnames=self.model_class.seralizable_fields,
            )
            writer.writeheader()
            writer.writerows(
                item.to_dict() for item in self.data.values()
            )

    def load(self) -> None:
        if not self.file_path.exists():
            return

        with self.file_path.open("r") as file:
            reader = DictReader(file)
            for row in reader:
                entity = self.model_class.from_dict(row)
                self.data[entity.id] = entity
