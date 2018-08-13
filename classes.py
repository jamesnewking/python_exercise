class Fruits(object):
    def __init__(self, name):
        self.name = name

    def nutrition(self):
        print("vitamin C")

    def shape(self):
        print("round")


class Watermelon(Fruits):
    def __init__(self):
        Fruits.__init__(self, 'watermelon')
        print('seedless watermelon')

    def nutrition(self):
        print('vitamin A')

    def color(self):
        print('Red')

f = Fruits('melon')
f.nutrition()
f.shape()

w = Watermelon()
w.nutrition()
w.color()
