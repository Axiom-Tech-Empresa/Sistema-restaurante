from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    return "Hello World"

if __name__ == "__main__":
    print("Configuração da URI do banco de dados:")
    print("")
    app.run(port=80, debug=True)