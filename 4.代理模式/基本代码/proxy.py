class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print('真实的请求')

class Proxy(Subject):
    def request(self):
        self.real = RealSubject()
        self.real.request()

if __name__ == '__main__':
    p = Proxy()
    p.request()
