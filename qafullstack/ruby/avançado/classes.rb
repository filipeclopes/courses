

class Conta
    attr_accessor :saldo, :nome
#construtor método que é executado toda vez que um método new é executado
    def initialize(nome)
        self.saldo = 0.0
        self.nome = nome
    end


    def deposita(valor)
        # self invoca um atributo dentro de uma classe
        self.saldo += valor
        #Interpolação de strings, usar aspas duplas e a variavel q qr interpolar vai entre #{}
        puts "Depositando a quantia de #{valor} reais na conta do #{self.nome}."
    end
end

c = Conta.new('Filipe')

c.deposita(100.00)
puts c.saldo

c.deposita(10.00)
puts c.saldo
puts c.nome