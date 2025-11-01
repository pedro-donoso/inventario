import os
import shutil
from datetime import datetime

ARCHIVO = 'inventario.txt'

def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'w', encoding='utf-8') as f:
            f.write("Camiseta Azul, 15 USD, 50 unidades, M\n")
            f.write("Pantalón Negro, 25 USD, 30 unidades, L\n")
            f.write("Chaqueta Roja, 40 USD, 20 unidades, S\n")
            f.write("Zapatillas Deportivas, 60 USD, 10 unidades, 42\n")
            f.write("Gorra Blanca, 10 USD, 100 unidades, Talla Única")


def leer_inventario():
    print("\n--- INVENTARIO COMPLETO ---")
    with open(ARCHIVO, 'r', encoding='utf-8') as f:
        print(f.read())


def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    talla = input("Talla: ")

    with open(ARCHIVO, 'a', encoding='utf-8') as f:
        f.write(f"\n{nombre}, {precio}, {cantidad}, {talla}")
    print("Producto agregado")

