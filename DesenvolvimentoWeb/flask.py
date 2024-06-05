# Implementar uma solução em Python com Flask que faça:
# a - Exiba a mensagem "Página Principal" no endereço raiz de uma página web.
# b - Exiba a mensagem: "Olá Mundo!" no endereço "/ola/" de uma pagina web.  
# c - Exiba a mensagem: "Olá Usuário!" no endereço "/ola/nome_do_usuario" de uma pagina web.  

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Página Principal"

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return "Olá, " + nome +"!"

if __name__ == '__main__':
    app.run()