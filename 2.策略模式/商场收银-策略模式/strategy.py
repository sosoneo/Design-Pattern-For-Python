class CashSuper:
    '''
    现金收取父类
    '''
    def accept_cash(self, money):
        return money

class CashNormal(CashSuper):
    '''
    正常收费类
    '''
    def accept_cash(self, money):
        return money

class CashRebate(CashSuper):
    '''
    折扣类
    '''
    def __init__(self,moneyRebate):
        '''
        :param moneyRebate: 折扣率
        '''
        if moneyRebate > 1 or moneyRebate < 0:
            print('折扣率错误, 折扣率初始化为1')
            moneyRebate = 1
        self.moneyRebate = moneyRebate
    def accept_cash(self, money):
        return money * self.moneyRebate

class CashReturn(CashSuper):
    '''
    返利类
    '''
    def __init__(self, moneyCondition, moneyReturn):
        '''
        :param moneyCondition: 满足返利的条件
        :param moneyReturn: 返利的金额
        '''
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn
    def accept_cash(self, money):
        if money >= self.moneyCondition:
            return money - (money // self.moneyCondition) * self.moneyReturn
        else:
            return money

class CashContext:
    '''
    收费策略Context
    '''
    def __init__(self, type):
        if type=="正常收费":
            self.cs = CashNormal()
        elif type=="满300返100":
            self.cs = CashReturn(300, 100)
        elif type=="打8折":
            self.cs = CashRebate(0.8)

    def get_request(self, money):
        return self.cs.accept_cash(money)

if __name__ == '__main__':
    print(CashContext("正常收费").get_request(300))
    print(CashContext("满300返100").get_request(300))
    print(CashContext("打8折").get_request((300)))