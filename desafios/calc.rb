
puts "Enter a num: "
num = gets.chomp.to_i
puts "Enter a operator: "
ope = gets.chomp
puts "Enter a second num: "
num2 = gets.chomp.to_i

if ope == "+"
    puts (num + num2)
elsif ope == "-"
    puts (num - num2)
elsif ope == "*"
    puts (num * num2)
elsif ope == "/"
    puts (num / num2)
else
    puts "Invalid count"
end
    
