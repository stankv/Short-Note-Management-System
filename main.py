from src.storage.category_storage import category_storage
from src.storage.note_storage import note_storage

def create_categories():
    category_storage.create(
        title="Домашние дела",
        description="Уборка, стирка, готовка",
    )
    category_storage.create(
        title="Работа",
        description="Проектирование, разработка, тестирование, деплой",
    )
    category_storage.create(
        title="Купить",
        description="Продукты, одежда, техника",
    )
    category_storage.create(
        title="Оплатить",
        description="ЖКХ, отопление, электричество",
    )

def create_notes():
    household_chores = category_storage.get_by_title("Домашние дела")
    job = category_storage.get_by_title("Работа")
    shopping = category_storage.get_by_title("Купить")
    pay = category_storage.get_by_title("Оплатить")

    # household_chores
    note_storage.create(
        title="Уборка гостинной",
        description="Сухая и влажная уборка, чистка ковра",
        tag="Уборка",
        category=household_chores,
    )
    note_storage.create(
        title="Постирать вещи",
        description="Постирать одежду, и занавески",
        tag="Стирка",
        category=household_chores,
    )
    note_storage.create(
        title="Приготовить обед",
        description="Сварить борщ, поджарить картошку, запечь курицу",
        tag="Готовка",
        category=household_chores,
    )

    # job
    note_storage.create(
        title="Проектирование системы управления заметками",
        description="Спроектировать систему в парадигме ООП",
        tag="Проектирование",
        category=job,
    )
    note_storage.create(
        title="Разработать модули спроектированной системы",
        description="Написать и протестировать код",
        tag="Кодинг",
        category=job,
    )
    note_storage.create(
        title="Деплой проекта",
        description="Развернуть проект на рабочем сервере",
        tag="Деплой",
        category=job,
    )

    # shopping
    note_storage.create(
        title="Хлеб",
        description="Круглый черный хлеб",
        tag="Продукты",
        category=shopping,
    )
    note_storage.create(
        title="Картофель",
        description="Картофель в Магните по 40р.",
        tag="Овощи",
        category=shopping,
    )
    note_storage.create(
        title="Куртка",
        description="Черная спортивная куртка в Ozon",
        tag="Одежда",
        category=shopping,
    )
    note_storage.create(
        title="Наушники",
        description="Беспроводные наушники Apple",
        tag="Техника",
        category=shopping,
    )

    # pay ЖКХ, отопление, электричество
    note_storage.create(
        title="Квитанции ЖКХ",
        description="Оплатить квитанции ЖКХ до 25-го",
        tag="Квитанции",
        category=pay,
    )
    note_storage.create(
        title="Счет за отопление",
        description="Оплатить счет за отопление до 12-го",
        tag="Отопление",
        category=pay,
    )
    note_storage.create(
        title="Счет за электричество",
        description="Снять показания счетчика и оплатить",
        tag="Готовка",
        category=pay,
    )



def main():
    if not category_storage.data:
        create_categories()
        print("Созданы новые категории заметок")
    if not note_storage.data:
        create_notes()
        print("Созданы новые заметки")
    all_categories = category_storage.get_all()
    for category in all_categories:
        print("Заметки категории", category.title)
        notes = note_storage.get_by_category(category)
        for note in notes:
            print("-", note)

        print()

if __name__ == "__main__":
    main()