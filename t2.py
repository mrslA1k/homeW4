print("Композиция, Наследование и Агрегирование.")
print(' ')
print("Композиция")
class Cls1:
    rep1 = 'Ага'

    def getCls1(self):
        return f'{self.rep1}'
class Cls2:
    rep2 = 'Уххх'

    def getCls2(self):
        return f'{self.rep2}'

    def getClsALL(self):
        r2 = self.rep2
        r1 = Cls1.rep1

        return f'{r2} агрегирутет с {r1}'

clsall = Cls2()
print(f'Композиция: {clsall.getClsALL()}')

print(' ')
print("Наследование")

class ParentClass:
    pstr = 'Parent'

    def getParent(self):
        return f'{self.pstr}'

class HildClass(ParentClass):
    hstr = 'Hild'

    def getHild(self):
        return f'{self.hstr}'

    def getInfo(self):
        return f'{self.hstr} наследует с {self.pstr}'

hcls = HildClass()
print(f'Наследование: {hcls.getInfo()}')


print("Bye")
input("жмякни Интер для выхода")
