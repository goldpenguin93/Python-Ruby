Class C
  def initialize(v)
    @value = value = v
  end
  def show()
    p @value
  end
  def getValue()
    return @value
end
def setValue(v)
  @value = v
  end
end
c1 = C.new(10)
#p c1.value
p c1.getValue()     #getValue = 관습적인 이름 //get = 가져오다.
#c1.value = 20
c1.setValue(20)     #setValue = 관습적인 이름 //set = 설정하다.
p c1.getValue()
