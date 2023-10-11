TimeList = {1900: "Винахід радіо",
            1969: "Перша у світі висадка на Місяць",
            2007: "Був представлений перший iPhone ",
            1994: "Була випущена перша PlayStation"} 

def GetAllEvents():
    for year, event in TimeList.items():
        print(f"У {year} відбулася подія: {event}")

def AddEvent(year, EventDescription):
    TimeList[year] = EventDescription
    print(f"Подія для {year} додана до словника часу")

def RemoveEvent(year):
    if year in TimeList:
        del TimeList[year]
        print(f"Подія для {year} видалена зі словника часу")
    else:
        print(f"Немає події для {year} у словнику часу")

while True:
    print("\nМеню:")
    print("1. Подивитися всі події за роками")
    print("2. Додати подію")
    print("3. Видалити подію")
    print("4. Вийти з програми")

    choice = input("Виберіть дію (1:2:3:4): ")

    if choice == '1':
        GetAllEvents()
    elif choice == '2':
        year = int(input("Введіть рік події: "))
        EventDescription = input("Введіть опис події: ")
        AddEvent(year, EventDescription)
    elif choice == '3':
        year = int(input("Введіть рік події, яку ви хочете видалити: "))
        RemoveEvent(year)
    elif choice == '4':
        print("Програма була завершена!")
        break
    else:
        print("Невірний вибір. Будь ласка, виберіть правильну дію.")
