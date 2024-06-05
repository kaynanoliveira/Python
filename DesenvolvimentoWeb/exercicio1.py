# Implementar uma solução em Python com Flask que faça:
# a - Exiba a mensagem "Olá, Programadores!" no endereço raiz de uma página web e apareça o link '/user/Usuario"
# b - Exiba a mensagem "Olá, Usuario!" no endereço "/user/" e exiba a mensagem "Altere o endereço do browser e recarregue a página".
# c - Exiba a mensagem "Olá, nome_usuario!" no endereço "/user/nome_do_usuario" de uma página web.

from flask import Flask
app = Flask(__name__)


