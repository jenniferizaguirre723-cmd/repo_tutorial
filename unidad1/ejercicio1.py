print("=== CAJA DEL KIOSCO ===")

nombre = input("Nombre del cliente: ").strip()

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Nombre del cliente: ").strip()

cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese una cantidad válida mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: ingrese un precio válido.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    descuento = input("¿Tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    total_sin_descuento += precio

    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuento += precio_final


ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n=== RESUMEN ===")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")