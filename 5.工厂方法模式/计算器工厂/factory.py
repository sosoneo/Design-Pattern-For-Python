class Operation:
    @property
    def numA(self):
        return self._numA

    @numA.setter
    def numA(self, number):
        self._numA = number

    @property
    def numB(self):
        return self._numB

    @numB.setter
    def numB(self, number):
        self._numB = number

    def getResult(self):
        pass

class AddOperation(Operation):
    def getResult(self):
        return self._numA + self._numB

class SubOperation(Operation):
    def getResult(self):
        return self._numA - self._numB

class MulOperation(Operation):
    def getResult(self):
        return self._numA * self._numB

class DivOperation(Operation):
    def getResult(self):
        try:
            return self.numA / self.numB
        except Exception as e:
            print(e)
            return 0

class IFactory:
    def creatOperation(self):
        pass

class AddFactory(IFactory):
    def creatOperation(self):
        return AddOperation()

class SubFactory(IFactory):
    def creatOperation(self):
        return SubOperation()

class MulFactory(IFactory):
    def creatOperation(self):
        return MulOperation()

class DivFactory(IFactory):
    def creatOperation(self):
        return DivFactory()

if __name__ == '__main__':
    op = AddFactory().creatOperation()
    op.numA = 1
    op.numB = 2
    print(op.getResult())