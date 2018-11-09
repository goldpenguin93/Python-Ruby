#파이썬의 메소드는 첫번째 매개변수를 정의해야합니다.
#첫번째 매게변수는 언제나 그 인스턴스가 됩니다. 그 인스턴스를 값을 매개변수를 가리킵니다.
#메소드를 호출할때 첫번째 매개변수로 첫번째 매개변수로 들어오는것을 약속되어있기때문에 첫번째 매개변수를 이용해서 인스턴스를 접근할수있다.
#self = s 변수의 이름
class Cal(object):
    def __init__(self,v1, v2):
        print(v1, v2)
        self.v1 = v1
        self.v2 = v2
    def add():
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
c1 = Cal(10,10)
print(c1,add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
