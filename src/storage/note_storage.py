from pathlib import Path

import settings
from src.models import Note, Category
from src.storage.csv_storage import CSVStorage


class NoteStorage(CSVStorage):
    """Хранение заметок"""
    def __init__(
            self,
            file_path: Path,
            model_class=Note,
    ):
        super().__init__(file_path, model_class)

    def create(
            self,
            title: str,
            description: str,
            tag: str,
            category: Category,
    ) -> Note:
        note = Note.create(
            title=title,
            description=description,
            tag=tag,
            category=category,
        )
        self.data[note.id] = note
        self.save()
        return note

    def get_by_category(self, category: Category) -> list[Note]:
        return [n for n in self.get_all() if n.category.id == category.id]

note_storage = NoteStorage(
    file_path=settings.NOTES_STORAGE_PATH,
)
note_storage.load()