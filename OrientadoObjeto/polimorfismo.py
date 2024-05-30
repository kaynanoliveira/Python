# Exemplo de Combustivel.

class Veiculo:
    def rodar(self):
        print('Reduz o consumo de Combustivel.')

class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print('Esse veículo possui Eletricidade.')

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()
