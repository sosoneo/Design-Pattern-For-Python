class Leifeng:
    def sweep(self):
        print('雷锋 扫地')

class Undergraduate(Leifeng):
    def sweep(self):
        print('大学生 扫地')

class Volunteer(Leifeng):
    def sweep(self):
        print('志愿者 扫地')

class IFactory:
    def creatFactory(self):
        pass

class LeiFengFactory(IFactory):
    def creatFactory(self):
        return Leifeng()

class UndergraduateFactory(IFactory):
    def creatFactory(self):
        return Undergraduate()

class VolunteerFactory(IFactory):
    def creatFactory(self):
        return Volunteer()

if __name__ == '__main__':
    l = LeiFengFactory().creatFactory()
    l.sweep()
