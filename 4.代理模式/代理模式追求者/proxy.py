class GiveGift:
    def giveDolls(self):
        pass
    def giveFlowers(self):
        pass
    def giveChocolate(self):
        pass

class Pursuit(GiveGift):
    def giveDolls(self):
        print('送你洋娃娃')
    def giveFlowers(self):
        print('送你花')
    def giveChocolate(self):
        print('送你巧克力')

class Proxy(GiveGift):
    def __init__(self):
        self.real = Pursuit()
    def giveDolls(self):
        self.real.giveDolls()
    def giveFlowers(self):
        self.real.giveFlowers()
    def giveChocolate(self):
        self.real.giveChocolate()

if __name__ == '__main__':
    p = Proxy()
    p.giveDolls()
    p.giveFlowers()
    p.giveChocolate()
