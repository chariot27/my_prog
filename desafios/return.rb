def cube(num)
    return num * num * num 
end

puts "Enter a num: "
input_num = gets
puts cube(input_num.to_i)
