from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulario de Login'
    return render_template('login.html')
@app.route('/produto')
def produto():
    return render_template('produto.html')

if __name__ == '__main__':
    app.run(debug=True)