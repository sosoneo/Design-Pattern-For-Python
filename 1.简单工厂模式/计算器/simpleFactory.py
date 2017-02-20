from enum import Enum, unique

class Operation(object):
    def __init__(self):
        self.numA = 0
        self.numB = 0
    def get_result(self):
        return 0

class OperationAdd(Operation):
    def get_result(self):
        return self.numA + self.numB

class OperationMinus(Operation):
    def get_result(self):
        return self.numA - self.numB

class OperationMultiply(Operation):
    def get_result(self):
        return  self.numA * self.numB

class OperationDivide(Operation):
    def get_result(self):
        try:
            return self.numA / self.numB
        except Exception as e:
            print(e)
            return 0

class OperationUnSport(Operation):
    def get_result(self):
        print('error unsport this operation')
        return 0

@unique
class OperationType(Enum):
    Add = 0
    Minus = 1
    Multiply = 2
    Divide = 3

class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationMinus()
    operation["*"] = OperationMultiply()
    operation["/"] = OperationDivide()
    def creat_operation(self, type):
        if type in self.operation:
            op = self.operation[type]
        else:
            op = OperationUnSport()
        return op

if __name__ == '__main__':
    type = input("operator: ")
    numA = input("a: ")
    numB = input("b: ")
    factory = OperationFactory()
    operation = factory.creat_operation(type)
    operation.numA = int(numA)
    operation.numB = int(numB)
    print(operation.get_result())