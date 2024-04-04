class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rastoen(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return distance

w = point(5,4)
print(w.rastoen())