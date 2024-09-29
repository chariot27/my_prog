file = File.open("teste.txt","r")
puts file.read

file.close

File.open("teste.txt", "w") do |file|
    file.write("\nOscar Accounting!!!")
end

File.open("index.html", "w") do |file|
    file.write("<h>Testes</h>")
end