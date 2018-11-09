#puts 대신 p를 사용합니다. p는 함수이고, ()을 생략해준다.
# subtract = 1빼는 값
#//생성자, constructor
#initialize = 초기화 약속된 메소드
#instance 값을 끌어 들어왔다.
# (10,10) @뒤에 오는것을 인스턴스 v1이다.
#변수이름앞에 @를 붙이면 됩니다.
#똑같은 객체에 속해 있기 때문에 연관성이 잘들어나있다.
#루비는 인스턴스값에 직접적으로 접근할수 없다. 그러기때문에 getv1 메소드를 사용해야한다.
class Cal
  attr_reader :v1, :v2
  attr_writer :v1
  @@_history = []                   #배열을 만드는 기호
  def initialize(v1, v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    result = @v1+@v2
    @@_history.push("add : #{@v1}+#{@v2}=#{result}")     #push라는 배열의 값을 추가하는것.
    return result
  end
  def subtract()
    result = @v1-@v2
    @@_history.push("add : #{@v1}-#{@v2}=#{result}")     #push라는 배열의 값을 추가하는것.
    return result
  end
  def setv1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getv1()
    return @v1
  end
def Cal.history()
  for item in @@_history
      p item
    end
  end
end
class CalMultiply < Cal
  def multiply()
    result = @v1*@v2
    @@_history.push("add : #{@v1}*#{@v2}=#{result}")     #push라는 배열의 값을 추가하는것.
    return result
  end
end
class CalDivide < CalMultiply
  def divide()
    result = @v1/@v2
    @@_history.push("add : #{@v1}/#{@v2}=#{result}")     #push라는 배열의 값을 추가하는것.
    return result
  end
end
#   def Cal.history()
#     for item in @@_history
#       p item
#     end
#   end
# end
c1 = CalMultiply.new(10,10)
p c1.add()
p c1.multiply()
c2 = CalMultiply.new(20, 10)
p c2, c2.add()
p c2, c2.multiply()
p c2, c2.divide()
Cal.history()

# c1 = Cal.new(10,10) #c1 인스턴드안에 매소드와 인스턴스변수가 아주 안전하게 보관되어있다. 다른코드와 변할수있는 확률이 적다
# p c1.add()
# p c1.subtract()
# c1.setv1('one')
# p c1.add()
