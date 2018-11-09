#getValue = 관습적인 이름 //get = 가져오다.
#setValue = 관습적인 이름 //set = 설정하다.
#value = 속성 = attribute
#reader와 writer 구분하는 이유는 읽기와 쓰기를 구분하기 편합니다.
Class C
  # attr_reader :value
  # attr_writer :value
  attr_accessor :value #읽기와쓰기가 가능한 함수이다.
  def initialize(v)
    @value = v                #value = v
  end
  def show()
    p @value
  end
end
c1 = C.new(10)
p c1.value                    #외부에서 접속하는 값.
# p c1.getValue()
c1.value = 20   # 20의 값은 value 값으로 사용한다. 오류가 나는 이유는 속성을 리더를 읽기가능하지만 쓰기는 안됩니다.
#p c1.getValue()
