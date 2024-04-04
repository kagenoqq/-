class car:
    def __init__(self, marka, speed):
        self.marka = marka
        self.speed = speed

    def max_speed(self, value):
        self.speed += value

w = car('vd', 60)
w.max_speed(90)
print(w.speed)
