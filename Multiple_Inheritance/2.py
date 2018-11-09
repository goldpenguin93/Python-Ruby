#method = function
#파이썬의 메소드는 첫번째 매개변수를 정의해야합니다.
#첫번째 매게변수는 언제나 그 인스턴스가 됩니다. 그 인스턴스를 값을 매개변수를 가리킵니다.
#메소드를 호출할때 첫번째 매개변수로 첫번째 매개변수로 들어오는것을 약속되어있기때문에 첫번째 매개변수를 이용해서 인스턴스를 접근할수있다.
#self = s 변수의 이름
#cal을 CalMultiply,CalDivide로 사용했다.

class CalMultiply():
    def multiply(self):
        return self.v1*self.v2
class CalDivide():
    def divide(self):
        return self.v1/self.v2
class Cal(CalMultiply, CalDivide):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    # def multiply(self):
    # return self.v1*self.v2
    def setv1(self, v):
        if isinstance(v, int):                 #만약 v가 숫자라면:
        self.v1 = v
    def getv1(self):
        return self.v1
    c= Cal(100, 10)
    print(c, add())
    print(c. multiply())
    print(c. divide())


c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())
c2 = CalDivide(20, 10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())


# c1 = Cal(10,10)
# print(c1.add())
# print(c1.subtract())
# c1.setv1 = ('one')
# c1.v2 = 30
# print(c1.add())
# print(c1.subtract())
