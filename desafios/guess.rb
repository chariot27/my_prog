secred_word = "giraffe"
guess = ""
count = 0
limit = 3
out_of_guesses = false

while guess != secred_word and !out_of_guesses
    if count < limit
        puts "Enter guess: "
        guess = gets.chomp()
        count += 1
    else
        out_of_guesses = true
    end

end

if out_of_guesses
    puts "You Lose"
else
    puts "You Won"
end