class Sample
    def hello
       puts "Hello Ruby!"
       puts "What's your name? "
       name = gets.chomp
       puts "Hello " + name + " Nice to meet you!"
       puts "Can you count up to 10 numbers from a list for me? "
       input = gets.chomp
       if input == "Sim" or input == "Yes"
            numbers = (1..10).to_a
            sum = 0
            numbers.each do |n|
                sum += n
            end
            puts sum

       else
            puts "Goodbye"
       end
    end
 end

 o = Sample. new
 o.hello
