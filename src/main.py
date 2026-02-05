from pathlib import Path
from uuid import uuid4

from src.models.category import Category
from src.storage.csv_storage import CSVStorage


def main():
    category = Category.create(
        title="Сделать",
        description="Покупки, уборка, мелкий ремонт, стирка",
    )
    print(category)
    print()
    print(category.to_dict())
    print()
    data = {
        "id": uuid4(),
        "title": "Купить",
        "description": "Продукты, одежда, чистящие средства, техника, мебель",
    }
    print("Новая категория из: ", data)
    new_category = Category.from_dict(data)
    print(new_category)
    print()
    print()
    category_filepath = Path(__file__).parent / "categories.csv"
    category_storage = CSVStorage(
        file_path=category_filepath,
        model_class=Category,
    )
    category_storage.data[category.id] = category
    category_storage.data[new_category.id] = new_category
    print(category_storage.data)
    category_storage.save()
    category_storage.load()
    print(category_storage.data)

if __name__ == "__main__":
    main()