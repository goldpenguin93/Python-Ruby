class C1
  def m()
    return 'parent'
  end
end
class C2 < C1
  def m()
    return m()+' child'
  end
end
