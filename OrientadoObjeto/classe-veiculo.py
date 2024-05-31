# Implementar um programa Python para criar uma classe Veiculo com atributos de instância "velocidade maxima" e "quilometros percorrido por litro"

class Veiculo:
    
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

# Função para imprimir os dados acima.

    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')

modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.toStr()

# Crie uma classe filha "Onibus" que herdará todas as Variaveis e metodos da classe "Veiculo".

class Onibus(Veiculo):
    pass

onibus_escolar = Onibus("Unitrans", 180, 10)
onibus_escolar.toStr()
