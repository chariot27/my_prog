def sayhi(name, age)
    puts "Hello User: "+ name
    puts "User Age: "+ age
end

puts "Enter a name: "
input_name = gets
puts "Enter your age: "
input_age = gets

sayhi(input_name, input_age)