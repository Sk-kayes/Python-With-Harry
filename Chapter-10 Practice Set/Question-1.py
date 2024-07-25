# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.


class Programmer():
    organization = "microsoft"

    def __init__ (self, id, name, language, skill, salary, pin):
        self.id = id
        self.name = name
        self.language = language
        self.skill = skill
        self.salary = salary
        self.pin = pin

kayes = Programmer(104, "Kayes", "Java", "Web", 10000000, 700121)
print(kayes.id, kayes.name, kayes.language, kayes.skill, kayes.salary, kayes.pin)

Albi = Programmer(102, "Albi", "Python", "Dsa", 5000000, 700193)
print(Albi.id, Albi.name, Albi.language, Albi.skill, Albi.salary, Albi.pin)
