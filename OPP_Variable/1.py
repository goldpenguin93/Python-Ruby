class C(object):
    def __init__(self, v):      #self= 매개변수를 만들면 첫번째 매개변수로 값으로 약속되어있다.
        self.value = v
    def show(self):
        print(self.value)

c1 = C(10)                      #10이라는 숫자가 인스턴스가 내부로 들어갑니다. #10은 v의값으로 들어간다.
print(c1.value)
c1.value = 20                   #value 값을 20으로 사용했습니다.
print(c1.value)
c1.show()
