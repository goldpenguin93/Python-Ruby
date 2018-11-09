class c1:
    def m(self):
        return 'parent'

class C2(c1):
    def m(self):
        return super().m() + 'child'            #super가 가르치는것은 메소드의 부모
     pass

o = C2()
print(o.m())          #o가 소속되는 m
