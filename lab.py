import random

item_sword = 0
question = 0
troff_dragon = 0

print("Ласкаво просимо до гри!\n\n\n")

# Початок історії
print("Ви опинилися в таємничому світі, де на кожному кроці таємничі пригоди чекають на вас.\n")
score = 0

# Перше питання
print("Вас атакують вороги, і ви потрапили в важку ситуацію.")
choice = input("Як ви дієте? (1 - Запустити закляття, 2 - Використати щит): ")

if choice == "1":
    print("Ви використали потужне закляття та знищили ворогів.")
    score += 10
else:
    print("Ви захистилися магічним щитом, але втратили частину балів.")
    score -= 5

# Друге питання
print("Ви подолали ворогів і продовжили свій шлях.\n")
print("Після деякого часу, ви потрапили в ліс, тут десь, сховано давній скарб.")
choice = input("Чи шукаєте ви цей скарб? (1 - Так, 2 - Ні): ")

if choice == "1":
    print("Слідуючи за подсвіченим шляхом, ви знайшли скарб і заробили додаткові бали!")
    score += 20
else:
    print("Ви вирішили не ризикувати і пішли далі лісом.")

# Третє питання
print("Ви продовжили свій шлях та потрапили до таємничого міста.\n")
print("У цьому місті, ви побачили підозрілого торгівця, що ві зробите?")
choice = input("Як ви дієте в цьому місті? (1 - Підійду, 2 - Уникну його): ")

if choice == "1":
    print("Ви вирішили підійти до нього і він сказав що віддасть сві меч якщо розгадати всі його загадки.")
if choice == "2":
    print("Ви обійшли торгівця.")

# Третє питання (загадки)
print("Торгівець загадав, вам першу загадку.\n")
print("Нехай легким буваю я, немов перо, бути довго і троллю зі мною нелегко.")
choice = input("Як ви дієте в цьому місті? (1 - Відьмак, 2 - Час ,3 - Відпочинок): ")

if choice == "1":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1
if choice == "2":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1
if choice == "3":
    print("І це првильно, ще дві загадки.")
    question += 1

print("Торгівець загадав, вам другу загадку.\n")
print("Один лечу легко й непомітно. Коли нас багато, важкі ми все одно. Я рани зцілюю, але відомо: перевірку мною пройти небагатьом судилося.")
choice = input("Як ви дієте в цьому місті? (1 - Годинник, 2 - Час ,3 - Таймер): ")

if choice == "1":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1
if choice == "2":
    print("І це првильно, ще одна загадки.")
    question += 1
if choice == "3":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1

print("Торгівець загадав, вам третю загадку.\n")
print("Я підношу удари і сюрпризи. Коли зла я - будеш у жертву принесений. Іронія - зносити мої примхи. Дарую подарунки я, і мною ти наділений.")
choice = input("Як ви дієте в цьому місті? (1 - Подарунок, 2 - Доля ,3 - Удача): ")

if choice == "1":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1
if choice == "2":
    print("І це првильно, ще одна загадки.")
    question += 1
if choice == "3":
    print("на жаль це не правильно і торгівець забрав ваші гроші.")
    score -= 1

print("Торгівець загадав, вам всі загадки.\n")
print("Ти відгадав моюзагадки ...")

if question == 3:
    print("... Ти правильно відгадав всі мої загадки, вот мій меч.")
    item_sword += 1
    print(f"Ваш меч: {item_sword}")
if question == 1:
    print("... Ти правильно відгадав лише одну мою загадку, я нічого тобі не дам.")

if question == 2:
    print("... Ти правильно відгадав лише дві мої загадки, я нічого тобі не дам.")

if question == 0:
    print("... Ти жодної загадки не відгадав.")
    print("*Вас вбили! Кінець")
    exit()

# П'яте питання
print("Після того як ви покинули місто, ви зіткнулися з великим драконом, який вам заважає.\n")
choice = input("Як ви дієте? (1 - Спробувати втекти, 2 - Боротися з драконом): ")

if choice == "1":
    if random.random() < 0.4:
        print("Ви вдало втекли від дракона та продовжили свою подорож.")
        print("Ви відважно втікали від дракона, і змогли до біжати до пещери і там сховатись.")
    else:
        print("Ви не змогли втекти від дракона.")
        print("Ви відважно втікали від дракона, але на жаль, не змогли.")
        exit()

if choice == "2":
    if item_sword == 1:
        print("Ви відважно боролися i перемогли його!")
        troff_dragon += 1
        item_sword -= 1
    else:
        print("Ви відважно боролися із драконом, але на жаль, не змогли його перемогти.")
        exit()


# Закінчення гри
print("Після декількох годин пригоди ви вирішили припинити свій пошук та повернутися в реальний світ.\n")
print("Гра завершилася.\n\n")
print(f"Ваш кінцевий рахунок: {score}")
print(f"Ваш трофей: {troff_dragon}")
exit()
