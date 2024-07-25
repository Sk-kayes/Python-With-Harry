class Employee:
    language = "python"
    salary = 120000

    def __init__(self):
        print("Creating first constructor")

    def __init__(self):
        print("Creating second constructor")

kayes = Employee()
print(kayes.language, kayes.salary)