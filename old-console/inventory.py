from datetime import datetime

# Inventario de Productos

def show_inventory(inventory):
    # Muestra los productos en el inventario
    if not inventory:
        print("El inventario está vacío.")
    else:
        print("\n" + "-" * 60)  
        print(f"{'Nombre':<20} {'Cantidad':<10} {'Precio ($)':<10} {'Fecha de Carga':<15}")
        print("-" * 60) 
        for product in inventory:
            print(f"{product['name']:<20} {product['quantity']:<10} {product['price']:.2f}      {product['date_added']:<15}")
        print("-" * 60)  
    print()  

def add_product(inventory):
    # Agrega un nuevo producto al inventario
    name = input("Ingresa el nombre del producto: ")

    # Validar cantidad
    while True:
        try:
            quantity = int(input("Ingresa la cantidad del producto (mínimo 1): "))
            if quantity < 1:
                print("La cantidad debe ser al menos 1. Intenta de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    # Validar precio
    while True:
        try:
            price = float(input("Ingresa el precio del producto (mínimo 0.01): "))
            if price < 0.01:
                print("El precio debe ser al menos 0.01. Intenta de nuevo.")
            # Comprobar que tenga máximo dos decimales
            elif round(price, 2) != price:
                print("El precio debe tener como máximo dos decimales. Intenta de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")

    date_added = datetime.now().strftime("%Y-%m-%d")  # Obtener fecha actual
    product = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "date_added": date_added
    }
    inventory.append(product)  # Agregar producto a la lista
    print(f"\nProducto '{name}' agregado exitosamente.\n")  

def menu():
    # Productos por defecto
    inventory = [
        {"name": "Manzanas", "quantity": 10, "price": 0.50, "date_added": datetime.now().strftime("%Y-%m-%d")},
        {"name": "Bananas", "quantity": 20, "price": 0.30, "date_added": datetime.now().strftime("%Y-%m-%d")},
        {"name": "Naranjas", "quantity": 15, "price": 0.40, "date_added": datetime.now().strftime("%Y-%m-%d")}
    ]
    
    while True:
        # Mostrar el menú principal
        print("\n" + "=" * 60)  
        print("Menú de Inventario")
        print("1. Agregar producto al inventario")
        print("2. Mostrar productos registrados")
        print("3. Salir")
        print("=" * 60)  
        
        option = input("Selecciona una opción (1-3): ")
        
        if option == '1':
            add_product(inventory)  # Llamar a la función para agregar producto
        elif option == '2':
            show_inventory(inventory)  # Llamar a la función para mostrar inventario
        elif option == '3':
            print("Saliendo del programa...")  # Mensaje de salida
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")  # Manejo de opción no válida

# Ejecutar el menú
if __name__ == "__main__":
    menu()  # Iniciar el programa
