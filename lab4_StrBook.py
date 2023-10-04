import random
import lorem
import string

# main class for page
class PageRegistrySingleton:
    _instance = None
    _current_page_id = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.page_ids = set()
        return cls._instance

    def get_next_page_id(self):
        while PageRegistrySingleton._current_page_id in self.page_ids:
            PageRegistrySingleton._current_page_id += 1
        page_id = PageRegistrySingleton._current_page_id
        self.page_ids.add(page_id)
        PageRegistrySingleton._current_page_id += 1
        return page_id

    def add_page_id(self, page_id):
        self.page_ids.add(page_id)

    def get_page_ids(self):
        return self.page_ids

# page
class Page:
    def __init__(self, content):
        self.content = content
        self.page_id = None

    def set_page_id(self, page_id):
        self.page_id = page_id

    def get_page_id(self):
        return self.page_id

# buider book
class BookBuilder:
    def __init__(self, title, author, genre):
        self.book = Book(title, author, genre)

    def add_page(self, content):
        page = Page(content)
        page_id = PageRegistrySingleton().get_next_page_id()
        page.set_page_id(page_id)
        self.book.add_page(page)

    def add_random_page(self, num_paragraphs, paragraphs_per_page):
        page_content = ""
        for _ in range(num_paragraphs):
            paragraph = [lorem.sentence() for _ in range(paragraphs_per_page)]
            page_content += "\n".join(paragraph)
            page_content += "\n\n"
        self.add_page(page_content)

    def set_format(self, book_format):
        self.book.format = book_format

    def get_book(self):
        return self.book

# book
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = []
        self.format = None

    def add_page(self, page):
        self.pages.append(page)

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Format: {self.format}")
        print("Pages:")
        for page in self.pages:
            print(f"Page ID: {page.get_page_id()}")
            print(page.content)
            print()

# manu
books = []

while True:
    print("\пГоловне меню:")
    print("1. Створити нову книгу")
    print("2. Додати сторінку до існуючої книги")
    print("3. Створити нову випадкову книгу")
    print("4. Переглянути всі наявні книги")
    print("5. Відкрити і прочитати книгу")
    print("6. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        title = input("Введіть назву книги: ")
        author = input("Введіть автора книги: ")
        genre = input("Введіть жанр книги: ")
        builder = BookBuilder(title, author, genre)

        while True:
            page_content = input("Введіть вміст сторінки (або 'exit' для завершення): ")
            if page_content.lower() == "exit":
                break
            builder.add_page(page_content)

        book_format = input("Введіть формат книги: ")
        builder.set_format(book_format)

        new_book = builder.get_book()
        books.append(new_book)
        new_book.display_info()

    elif choice == "2":
        # 2 add page
        if books:
            print("Виберіть книгу, до якої ви хочете додати сторінку::")
            for i, book in enumerate(books):
                print(f"{i + 1}. {book.title}")
            book_choice = int(input("Виберіть номер книги: ")) - 1
            if 0 <= book_choice < len(books):
                page_content = input("Введіть вміст сторінки (або 'exit' для завершення): ")
                if page_content.lower() == "exit":
                    continue
                books[book_choice].add_page(page_content)
            else:
                print("Некоректний номер книги.")
        else:
            print("Спочатку створіть книгу.")

    elif choice == "3":
        # Create Random book
        title = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15)))
        author = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15)))
        genre = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15)))
        builder = BookBuilder(title, author, genre)

        num_pages = int(input("Введіть кількість сторінок для випадкової книги: "))
        paragraphs_per_page = int(input("ведіть кількість абзаців на сторінці: "))

        for _ in range(num_pages):
            builder.add_random_page(num_paragraphs=paragraphs_per_page, paragraphs_per_page=paragraphs_per_page)

        book_format = input("Введіть формат книги: ")
        builder.set_format(book_format)

        random_book = builder.get_book()
        books.append(random_book)
        random_book.display_info()

    elif choice == "4":
        # All BOOK
        if books:
            print("\nВсе существующие книги:")
            for i, book in enumerate(books):
                print(f"{i + 1}. {book.title} by {book.author}")
        else:
            print("Немає існуючих книг.")

    elif choice == "5":
        if books:
            print("\nВиберіть книгу для відкриття і читання:")
            for i, book in enumerate(books):
                print(f"{i + 1}. {book.title} by {book.author}")
            book_choice = int(input("Виберіть номер книги: ")) - 1
            if 0 <= book_choice < len(books):
                print("\nВміст книги:")
                for page in books[book_choice].pages:
                    if isinstance(page, Page):  # Проверяем тип объекта
                        print(f"Page ID: {page.get_page_id()}")
                        print(page.content)
                        print()
                    else:
                        print("ERROR: Це не сторінка книги.")
            else:
                print("Некоректний номер книги.")
        else:
            print("Немає існуючих книг") #Нет существующих книг

    elif choice == "6":
        print("exit!")
        break
