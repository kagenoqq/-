class employee:
    def __init__(self, name, position, zp):
        self.name = name
        self.position = position
        self.zp = zp

    def max_zp(self, value):
        self.zp += value

w = employee('имя', 'должность', 50000)
print('зарплата:', w.zp)
w.max_zp(2000)
print('зарплата после повышения:', w.zp)