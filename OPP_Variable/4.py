class C(object):
    def __init__(self, v):      #self= 매개변수를 만들면 첫번째 매개변수로 값으로 약속되어있다.
        self.__value = v
    def show(self):
        print(self.value)
c1 = c(10)
# print(c1.__Value)
c1.show()

    # def getValue(self):
    #     return self.value
    # def setValue(self, v):
    #     self.value = v

#
# c1 = C(10)                      #10이라는 숫자가 인스턴스가 내부로 들어갑니다. #10은 v의값으로 들어간다.
# print(c1.value)                 #python은 기본적으로 속성값을 인스턴스 외부에서 접근 가능하다.



# print(c1.getValue())
# # c1.value = 20                   #value 값을 20으로 사용했습니다.
# c1.setValue(20)
# print(c1.getValue())
# # c1.show()
