class Compoent:
    def operation(self):
        pass

class ConcreateComponent(Compoent):
    def operation(self):
        print('具体的操作')

class Decorator(ConcreateComponent):
    def behavior(self, compoent):
        self.compoent = compoent

    def operation(self):
        if self.compoent:
            self.compoent.operation()

class DecoratorA(Decorator):
    def operation(self):
        print('操作a')
        self.compoent.operation()

class DecoratorB(Decorator):
    def operation(self):
        print('操作b')
        self.compoent.operation()

if __name__ == '__main__':
    c = ConcreateComponent()
    d1 = DecoratorA()
    d2 = DecoratorB()
    d2.behavior(c)
    d1.behavior(d2)
    d1.operation()
