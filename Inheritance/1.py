#inheritance = 상속
#인스턴스값이 c1이다.
#상속은 중복제거가 핵심이다.
#class3는 class1의 기능을 가지면서 class1의 값을 사용하고있다






class Class1(object):
    def method1(self):return 'm1'
c1 = Class1()
print(c1, c1.method1())

class Class3(Class1):
    def method2(self): return 'm2'
c3 = Class3()
print(c3, c3.method1())

class Class2(object):
    def method1(self):return 'm1'
    def method2(self):return 'm2'
c2 = Class2()
print(c2.method1())
print(c2.method2())
