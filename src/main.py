from uuid import uuid4

from src.models.category import Category

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

if __name__ == "__main__":
    main()