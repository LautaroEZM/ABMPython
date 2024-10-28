from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

# Cargar inventario desde un archivo
def load_inventory():
    if os.path.exists('inventory.txt'):
        with open('inventory.txt', 'r') as file:
            return json.load(file)
    return []

# Guardar inventario en un archivo
def save_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        json.dump(inventory, file)

# Inventario de Productos
inventory = load_inventory()  # Cargar inventario al iniciar

@app.route('/')
def index():
    return render_template('inventory.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    date_added = datetime.now().strftime("%Y-%m-%d")

    product = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "date_added": date_added
    }
    inventory.append(product)  # Agregar producto a la lista
    save_inventory(inventory)  # Guardar inventario en el archivo

    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_product(index):
    if 0 <= index < len(inventory):
        inventory.pop(index)  # Eliminar producto de la lista
        save_inventory(inventory)  # Guardar cambios en el archivo
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
