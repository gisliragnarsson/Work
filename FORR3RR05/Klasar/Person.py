class Person:
    def __init__(self, n, a, h, l):
        self.name = n
        self.age = a
        self.hair = h
        self.languages = l
    
    def changeName(self, newAge):
        self.name = newAge
    
    def increaseAge(self):
        self.age += 1

    def changeHair(self, newHair):
        self.hair = newHair
    
    def addLanguage(self, newLanguage):
        self.languages.append(newLanguage)

    def languageCount(self):
        return len(self.languages)

p = Person("John", 32, "brown", ["Icelandic", "English"])


p.changeName("Jane")
print(p.name) # Prentast út "Jane"


p.increaseAge()
p.increaseAge()
print(p.age) # Prentast út 34


p.changeHair("yellow")
print(p.hair) # Prentast út "yellow"


print(p.languageCount()) # Prentast út 2
p.addLanguage("Danish")
print(p.languageCount()) # Prentast út 3