from uuid import uuid4

from src.models.category import Category
from src.models.note import Note
from src.storage.csv_storage import CSVStorage
from src.storage.category_storage import category_storage

from settings import CATEGORIES_STORAGE_PATH, NOTES_STORAGE_PATH


def print_data(data: dict):
    for key, value in data.items():
        print(key, value)
    print()


def demo_create_and_read():
    category = Category.create(
        title="Сделать",
        description="Покупки, уборка, мелкий ремонт, стирка",
    )
    print(category)
    print(category.title, "|", category.description)
    print()
    print(category.to_dict())
    print()
    data = {
        "id": uuid4(),
        "title": "Купить",
        "description": "Продукты, одежда, чистящие средства, техника, мебель",
    }
    print("Новая категория: ", data)
    new_category = Category.from_dict(data)
    print(new_category)
    print(new_category.title, "|", new_category.description)
    print()
    print()
    category_storage = CSVStorage(
        file_path=CATEGORIES_STORAGE_PATH,
        model_class=Category,
    )
    category_storage.load()
    print_data(category_storage.data)
    category_storage.data[category.id] = category
    category_storage.data[new_category.id] = new_category
    print(category_storage.data)
    category_storage.save()
    print_data(category_storage.data)

def example_category_storage():
    category = category_storage.create(
        title="Оплатить квитанции",
        description="ЖКХ, Отопление, Электричество, Налог на имущество"
    )
    print(category)
    print()

    for k in category_storage.get_all():
        print(k)
    print()

    dishes_category = category_storage.get_by_title("Сделать")
    print("Найдена категория:")
    print(dishes_category)

def main():
    category = category_storage.get_by_title("Купить")
    fork = Note.create(
        title="Огурцы",
        description="Огурцы грунтовые в Пятерочке по 177 руб.",
        tag="Покупки",
        category=category,
    )
    print(fork)

    storage = CSVStorage(
        file_path=NOTES_STORAGE_PATH,
        model_class=Note,
    )
    storage.data[fork.id] = fork
    storage.save()
    storage.load()
    print_data(storage.data)
    for note in storage.data.values():
        print(type(note.category))
        print(note.category)

if __name__ == "__main__":
    main()