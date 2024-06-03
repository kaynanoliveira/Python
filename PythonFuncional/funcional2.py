# Implemetar uma solução através da Programação Funcional para transformar todos os nomes em Maiusculos.

veiculos = ['Avião', 'Carro', 'Navio', 'Ônibus']

# Estratégia 01
print(list(map(lambda veiculos: veiculos.upper(), veiculos)))

# Estratégia 02
f_maiuscula = lambda x: str.upper(x)
nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'Nomes Maiusculos: {nomes_maiusculos}')