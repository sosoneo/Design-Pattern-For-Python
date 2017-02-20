class Strategy:
    '''
    抽象算法类
    '''
    def algorithmInterface(self):
        '''
        算法方法
        '''
        pass

class ConcreteStrategyA(Strategy):
    '''
    具体算法a
    '''
    def algorithmInterface(self):
        print('算法a的实现')

class ConcreteStrategyB(Strategy):
    '''
    具体算法b
    '''
    def algorithmInterface(self):
        print('算法b的实现')

class ConcreteStrategyC(Strategy):
    '''
    具体算法c
    '''
    def algorithmInterface(self):
        print('算法c的实现')

class Context:
    '''
    上下文
    '''
    def __init__(self, strategy):
        self.strategy = strategy

    def algorithmInterface(self):
        self.strategy.algorithmInterface()

if __name__ == '__main__':
    conA = Context(ConcreteStrategyA())
    conB = Context(ConcreteStrategyB())
    conC = Context(ConcreteStrategyC())

    conA.algorithmInterface()
    conB.algorithmInterface()
    conC.algorithmInterface()








