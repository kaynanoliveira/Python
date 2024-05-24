#Exemplo de Lista Sequencial 
lista = [101, 102, 103, 104, 105]
print(f"lista[0] = {lista[0]}")
print(f"lista[1] = {lista[1]}")
print(f"lista[2] = {lista[2]}")
print(f"lista[3] = {lista[3]}")
print(f"lista[4] = {lista[4]}")
print(f"Lista completa: {lista}")
#Exemplo de Dicionário
pessoas={1111:["Kaynan"], 2222:["Julia"], 3333:["Lucas"], 4444:["Kevin"]}
print(f"Primeira pessoa = {pessoas[1111]}")
print(f"Segunda pessoa = {pessoas[2222]}")
# A variável a passa a ser composta dos itens ‘UF’ e ‘RN’. Assim, a chamada len(a) retorna o tamanho 2, número de elementos de a.
a = ['U'] + ['RN']
print(len(a))
# A variável b passa a ser a lista ['4', '4', '4', '4']. E a chamada len(b) retorna o tamanho 4, número de elementos de b.
b = ['4'] * 4
print(len(b))