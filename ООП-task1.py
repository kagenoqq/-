class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def plosched(self):
        return self.width * self.height

w = rectangle(5, 10)
print(w.plosched())
