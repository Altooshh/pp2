class StringManipulator:
    def __init__(self):
        self.text = ""

    # Метод для получения строки с консоли
    def getString(self):
        self.text = input("Enter a string: ")

    # Метод для печати строки в верхнем регистре
    def printString(self):
        if self.text:  # Проверим, что текст не пустой
            print(self.text.upper())
        else:
            print("No text entered")

# Создание объекта класса
string_manipulator = StringManipulator()

# Вызов методов
string_manipulator.getString()  # Запрашивает строку у пользователя
string_manipulator.printString()  # Печатает строку в верхнем регистре




class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    p1=Person("John",36)

    print(p1.name)
    print(p2.age)