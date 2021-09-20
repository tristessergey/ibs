class Animal():
    def voice(self):
        pass

class A(Animal):
    def voice(self):
        print('rrrr')

class B(Animal):
    def voice(self):
        print('meow')

class C(Animal):
    def voice(self):
        print('rwrw')

pet1 = A()
pet2 = B()
pet3 = C()

pet1.voice()
pet2.voice()
pet3.voice()
