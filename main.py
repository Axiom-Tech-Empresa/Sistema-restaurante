from db_config import app
import models.models

@app.route('/')
def init():
    return "Hello World"

if __name__ == "__main__":
    print("Iniciando o servidor Flask...")
    # Usamos o 'app' importado para rodar a aplicação
    app.run(port=80, debug=True)