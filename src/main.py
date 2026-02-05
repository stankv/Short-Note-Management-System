from src.models.category import Category

def main():
    category = Category.create(
        title="Сделать",
        description="Покупки, уборка, мелкий ремонт, стирка",
    )
    print(category)

if __name__ == "__main__":
    main()