class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("装扮的 %s" % self.name)

class Finery(Person):
    def decorate(self, component):
        self.component = component
    def show(self):
        if self.component:
            self.component.show()

class TShirts(Finery):
    def __init__(self):
        pass
    def show(self):
        print('装扮的T恤')
        self.component.show()

class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print("装扮的大裤子")
        self.component.show()

if __name__ == '__main__':
    p = Person("sosoneo")
    bt = BigTrouser()
    ts = TShirts()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()