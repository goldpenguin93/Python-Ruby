#다중상속은 제한된 공간에서는 사용하기 쉽다.
#단점은 주먹구구식 이기때문에 다중상속은 신중을 기이해야한다. 대안으로는 믹스인 언어가 있다.

class c1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("c1 m")
class c2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

class c3(c1, c2):
    def m(self):
        print("c3 m")

c = c3()
c.c1_m()
c.c2_m()
c.m()
print(c3.__mro__)
