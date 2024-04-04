class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ages(self):
        year = 2024
        return f'{self.name}, вам {year - self.age}'

w = person('имя', 1999)
print(w.ages())