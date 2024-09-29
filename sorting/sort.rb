class SortNumbers
  def sortear
    numbers = [31,41,59,26,41,58] 
    list = numbers.sort
    puts list.inspect
  end
end

s = SortNumbers.new
s.sortear
