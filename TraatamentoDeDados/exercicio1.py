# Carregar os dados da base load_digits. Informar a quantidade de dados.

from sklearn.datasets import load_digits
digitos = load_digits()

# Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64)
print("Shape dos dados de imagem:{}".format(digitos.data.shape))

# Apresentar o resultados de dados rotulados com inteiros de 0 a 9.
print("Shape dos dados rotulados:{}".format(digitos.target.shape))