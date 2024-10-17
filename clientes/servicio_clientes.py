from flask import Flask, jsonify

app = Flask(__name__)

# Definimos una ruta para obtener la lista de clientes
@app.route('/clientes')
def get_clientes():
    return jsonify({"clientes": ["cliente1", "cliente2", "cliente3"]})

if __name__ == "__main__":
    app.run(port=5001)