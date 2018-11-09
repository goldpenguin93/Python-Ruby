#루비에서 메소드가 클래스의 소속이라면 실행할때 클래스소속이라고 표시해야합니다.
#클래스 멤버는 인스턴스에서 사용할수없을때, 인스턴스에서도 클래스에서도 사용할수없다.
#클래스는 인스턴스소속에 속한다, 인스턴스소속은 클래스에 소속된다.

class Cs
  def Cs.class_method()
    p "Class method"
  end
    def instance_method()
      p "Instance_method"
  end
end
i = Cs.new()
Cs.class_method()
i.instance_method() #i = cs를 인스턴스화 한것을 i이다.
# Cs.instance_method()
# i.class_method()
