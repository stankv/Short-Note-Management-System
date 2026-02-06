from pathlib import Path

import settings
from src.models.category import Category
from src.storage.csv_storage import CSVStorage


class CategoryStorage(CSVStorage):
    """Хранение типов заметок"""
    def __init__(
            self,
            filepath: Path,
            model_class=Category,
    ):
        super().__init__(filepath, model_class)

    def create(self, title: str, description: str) -> Category:
        category = Category.create(title, description)
        self.data[category.id] = category
        self.save()
        return category

    def get_all(self) -> list[Category]:
        return list(self.data.values())

    def get_by_title(self, title: str) -> Category | None:
        for category in self.get_all():
            if category.title == title:
                return category
        return None

category_storage = CategoryStorage(
    filepath=settings.CATEGORIES_STORAGE_PATH,
)
category_storage.load()
