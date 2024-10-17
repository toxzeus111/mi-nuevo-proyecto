from flask import Flask, jsonify

app = Flask(__name__)

# Definimos una ruta para obtener la lista de compras
@app.route('/compras')
def get_compras():
    return jsonify({"compras": ["compra1", "compra2", "compra3"]})

# Definimos una ruta para obtener las compras de un cliente específico
@app.route('/compras/cliente/<int:cliente_id>')
def get_compras_por_cliente(cliente_id):
    return jsonify({"compras": [f"compra{cliente_id}-1", f"compra{cliente_id}-2"]})

if __name__ == "__main__":
    app.run(port=5002)