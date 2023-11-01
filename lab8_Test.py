import random

defaultAnswers = [
    "Так",
    "Ні",
    "Можливо",
    "Сконцентруйся та спробуй знову",
    "Не маю певності",
    "Це можливо в майбутньому",
    "Можливо, але не розраховуй на це",
]

def charivnaKulka(question: str) -> str:
    if not isinstance(question, str) or question.strip() == "":
        return "Будь ласка, поставте конкретне питання."

    return random.choice(defaultAnswers)

# Тести
def testCharivnaKulkaReturn():
    answer = charivnaKulka("Чи сьогодні буде дощ?")
    assert answer in defaultAnswers

def testCharivnaKulkaReturnType():
    answer = charivnaKulka("Питання про тип")
    assert isinstance(answer, str)

def testCharivnaKulkaEmptyQuestion():
    answer = charivnaKulka("")
    assert answer == "Будь ласка, поставте конкретне питання."

def testCharivnaKulkaNonStringInput():
    answer = charivnaKulka(123)
    assert answer == "Будь ласка, поставте конкретне питання."

# Запуск тестів
testCharivnaKulkaReturn()
testCharivnaKulkaReturnType()
testCharivnaKulkaEmptyQuestion()
testCharivnaKulkaNonStringInput()
