#클래스멤버에 종류에는 클래스 메소드와 스태틱 메소드가 있다.
#인스턴스에 소속된것은 인스턴스멤버다.
#cs = 클래스
#i = 인스턴스
class Cs:
    @staticmethod
    def static_method():
        print("Static method")
    @classmethod
    def class_method(cls):          #첫번째 매개변수(cls)가 있어야합니다.
        print("Class method")
    def instance_method(self):      #첫번째 인자값(self)을 준다.
        print("Instance_method")
i = Cs()
Cs.static_method()                  #클래스 멤버는 스태틱메소드의 멤버이다.
Cs.class_method()                   #클래스 멤버는 클래스메소드의 멤버이다.
i.instance_method()                 #인스턴스 멤버는 인스턴스의 멤버이다.
