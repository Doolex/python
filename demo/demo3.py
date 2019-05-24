class demo3:
    def say(self):
        print(self)


class demo4(demo3):
    def __init__(self):
        print(self.__class__)

    def say1(self):
        print("子类输出")
