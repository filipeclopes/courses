#-- criar loops, numero.times

# 5.times do |i|
#   puts 'Repetindo a mensagem ' + i.to_s + ' vez(es).' 
# end

#-- Uso do while, variável de incremento

# init = 0
# while init <= 10 do
#   puts 'Repetindo a mensagem ' + init.to_s + ' vez(es).'
#   init += 1
# end

#-- Uso do For

# for item in (0...10)
#   puts 'Repetindo a mensagem ' + item.to_s + ' vez(es).'
# end

# Uso de Arrays - for each

vingadores = ['Ironman', 'Hulk', 'Spiderman', 'Thor']
vingadores.each do |v|
  puts v
end