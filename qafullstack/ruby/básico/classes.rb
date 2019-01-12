# Ruby é uma linguagem considerada puramente orientada a objetos
# Pq no Ruby tudo são objetos

# Classe forma de organizar atributos e métodos
# Caracteristicas e Ações

# Carro (Nome, Marca, Modelo, Cor, quantidade de portas, etc..)
# Ligar, Buzinar, Parar, etc...

class Carro
    attr_accessor :nome
    
    def ligar
        puts 'O carro está pronto para iniciar o trajeto.'
    end
end

civic = Carro.new
civic.nome = 'Civic'
puts civic.nome 
civic.ligar