#p=()
#@value #루비에서 인스턴스를 가리키는 변수
#initialize =ruby에서의 생성자
Class C
def initialize(v)

    @value = v
end
  def show()
    p @value 
  end
end
c1 = C.new(10)
# p c1.value
# c1.value = 20
c1 = show()
