import csv
import os

class BookDatabase:
    def __init__(self, database_file):
        self.database_file = database_file
        self.headers = ["Id", "email", "address", "phone"]

    def create_database(self):
        with open(self.database_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)

            initial_data = [
                ["Книга 1", "Автор 1", 2020, "Фантастика"],
                ["Книга 2", "Автор 2", 2019, "Драма"],
                ["Книга 3", "Автор 3", 2021, "Пригоди"],
                ["Книга 4", "Автор 4", 2018, "Фентезі"],
                ["Книга 5", "Автор 5", 2022, "Жахи"]
            ]

            writer.writerows(initial_data)

    def add_book(self, book):
        with open(self.database_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(book)

    def read_database(self):
        with open(self.database_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

    def search(self, criteria):
        with open(self.database_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            found = False
            for row in reader:
                if criteria in row:
                    print(row)
                    found = True

            if not found:
                print(f"Записи, що відповідають критерію '{criteria}', не знайдено.")

    def update(self, criteria, new_data):
        data = []
        with open(self.database_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        for row in data:
            if criteria in row:
                row[2] = new_data

        with open(self.database_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([self.headers] + data)

    def delete(self, criteria):
        data = []
        with open(self.database_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            data = list(reader)

        data = [row for row in data if criteria not in row]

        with open(self.database_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([self.headers] + data)

database = BookDatabase('BaseDate.csv')
database.create_database()

while True:
    print("Меню:")
    print("1. Додати книгу")
    print("2. Пошук")
    print("3. Переглянути базу даних")
    print("4. Оновити запис")
    print("5. Видалити запис")
    print("6. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        title = input("Назва книги: ")
        author = input("Автор: ")
        year = int(input("Рік видання: "))
        genre = input("Жанр: ")

        database.add_book([title, author, year, genre])
        print("Книгу додано до бази даних.")
    elif choice == '2':
        criteria = input("Введіть критерій пошуку: ")
        database.search(criteria)
    elif choice == '3':
        print("База даних книг:")
        database.read_database()
    elif choice == '4':
        criteria = input("Введіть критерій оновлення: ")
        new_data = input("Введіть нові дані: ")
        database.update(criteria, new_data)
    elif choice == '5':
        criteria = input("Введіть критерій видалення: ")
        database.delete(criteria)
        print("Запис видалено з бази даних.")
    elif choice == '6':
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
