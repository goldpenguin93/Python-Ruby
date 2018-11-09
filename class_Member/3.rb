#@couunt 클래스에 속한다
#@@count  인스턴스에 속한다.
#@getCount = 몇개의 인스턴스를 생성됬는지 확인해준다.
#@@count = @@count + 1
class Cs
  @@count = 0
  def initialize()
    @@count = @@count + 1
  end
  def Cs.getCount()
    return @@count
  end
end
i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
# p Cs.getCount()
