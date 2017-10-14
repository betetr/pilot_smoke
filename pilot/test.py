def log(name):
    def prt1(func):
        def warp(*args, **kw):
            print(name, end='')
            for i in range(30):
                print('*', end='')
            print('')
            func(*args, **kw)
            print(name, end='')
            for i in range(30):
                print('*', end='')
            print('')
            return func
        return warp
    return prt1

class scr0(object):
    def scrp0(self):
        print('today is yesterday')

class scr(scr0):
    def scrp1(self):
        self.scrp0()
        print('today is wensday')

    @log('test')
    def scrp2(self):
        self.scrp1()
        print('today is monday')
        self.scrp1()

if __name__=='__main__':
    ps = scr()
    ps.scrp2()