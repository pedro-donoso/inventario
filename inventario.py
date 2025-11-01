import os

import shutil

from datetime import datetime

ARCHIVO = "inventario.txt"


def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("Camiseta Azul, 15 USD, 50 unidades, M\n")
            f.write("Pantalón Negro, 25 USD, 30 unidades, L\n")
            f.write("Chaqueta Roja, 40 USD, 20 unidades, S\n")
            f.write("Zapatillas Deportivas, 60 USD, 10 unidades, 42\n")
            f.write("Gorra Blanca, 10 USD, 100 unidades, Talla Única")


def leer_inventario():
    print("\n--- INVENTARIO COMPLETO ---")
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        print(f.read())


def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    talla = input("Talla: ")

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"\n{nombre}, {precio}, {cantidad}, {talla}")
    print("Producto agregado")


def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    busqueda = input("Nombre del producto: ").lower()
    
    encontrado = False
    with open(ARCHIVO, 'r', encoding='utf-8') as f:
        for linea in f:
            if busqueda in linea.lower():
                print(f"✓ Encontrado: {linea.strip()}")
                encontrado = True
    
    if not encontrado:
        print("✗ No encontrado")


def modificar_producto():
    print("\n--- MODIFICAR PRODUCTO ---")
    busqueda = input("Nombre del producto a modificar: ").lower()

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    nuevas_lineas = []
    encontrado = False

    for linea in lineas:
        if busqueda in linea.lower() and not encontrado:
            print(f"Encontrado: {linea.strip()}")
            nuevo = input("Nueva línea completa: ")
            nuevas_lineas.append(nuevo + "\n")
            encontrado = True
        else:
            nuevas_lineas.append(linea)

    if encontrado:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.writelines(nuevas_lineas)
        print("Producto modificado")
    else:
        print("No encontrado")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    busqueda = input("Nombre del producto a eliminar: ").lower()

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    nuevas_lineas = [l for l in lineas if busqueda not in l.lower()]

    if len(nuevas_lineas) < len(lineas):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.writelines(nuevas_lineas)
        print("Producto eliminado")
    else:
        print("No encontrado")


def ver_atributos():
    print("\n--- ATRIBUTOS DEL ARCHIVO ---")
    tamano = os.path.getsize(ARCHIVO)
    fecha = datetime.fromtimestamp(os.path.getmtime(ARCHIVO))

    with open(ARCHIVO, "r") as f:
        productos = len(f.readlines())

    print(f"Tamaño: {tamano} bytes")
    print(f"Última modificación: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Productos: {productos}")


def crear_backup():
    print("\n--- CREAR BACKUP ---")
    if not os.path.exists("backups"):
        os.makedirs("backups")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = f"backups/inventario_{timestamp}.txt"
    shutil.copy2(ARCHIVO, backup)
    print(f"Backup creado: {backup}")


def menu():
    crear_archivo_inicial()

    while True:
        print("\n=== MODA XPRESS ===")
        print("1. Ver inventario")
        print("2. Registrar producto")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Ver atributos")
        print("7. Crear backup")
        print("0. Salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == '1': leer_inventario()
        elif opcion == '2': registrar_producto()
        elif opcion == '3': buscar_producto()
        elif opcion == '4': modificar_producto()
        elif opcion == '5': eliminar_producto()
        elif opcion == '6': ver_atributos()
        elif opcion == '7': crear_backup()
        elif opcion == '0': 
            print("¡Hasta pronto!")
            break
        else: print("Opción inválida")
        
if __name__ == "__main__":
    menu()
        
