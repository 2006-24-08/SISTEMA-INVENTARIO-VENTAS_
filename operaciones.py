import os
from datetime import datetime

# Archivos del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE_DIR, "inventario.csv")
LOG = os.path.join(BASE_DIR, "bitacora.txt")

# Lista donde se guardan las ventas
ventas = []


def registrar_log(mensaje):
    """Guarda las operaciones realizadas en la bitácora."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    archivo = open(LOG, "a", encoding="utf-8")
    archivo.write(f"[{fecha}] {mensaje}\n")
    archivo.close()


def cargar_inventario():
    """Carga los productos desde el archivo CSV."""
    inventario = []

    try:
        if not os.path.exists(CSV):
            archivo = open(CSV, "w", encoding="utf-8")
            archivo.write("codigo,nombre,precio,stock,categoria\n")
            archivo.close()
            return inventario

        archivo = open(CSV, "r", encoding="utf-8")

        lineas = archivo.readlines()

        for linea in lineas[1:]:
            datos = linea.strip().split(",")

            if len(datos) == 5:
                producto = {
                    "codigo": datos[0],
                    "nombre": datos[1],
                    "precio": float(datos[2]),
                    "stock": int(datos[3]),
                    "categoria": datos[4]
                }

                inventario.append(producto)

        archivo.close()

    except ValueError:
        print("Error: hay un dato incorrecto en el archivo de inventario.")

    except Exception:
        print("Error al cargar el inventario.")

    return inventario


def guardar_inventario(inventario):
    """Guarda el inventario en el archivo CSV."""

    archivo = open(CSV, "w", encoding="utf-8")

    archivo.write("codigo,nombre,precio,stock,categoria\n")

    for producto in inventario:
        archivo.write(
            f"{producto['codigo']},"
            f"{producto['nombre']},"
            f"{producto['precio']},"
            f"{producto['stock']},"
            f"{producto['categoria']}\n"
        )

    archivo.close()


def mostrar_inventario(inventario):
    """Muestra el inventario ordenado."""

    print("\n¿Cómo deseas ordenar?")
    print("1. Por nombre")
    print("2. Por precio")

    opcion = input("Opción: ")

    if opcion == "1":
        inventario.sort(key=lambda x: x["nombre"])
    elif opcion == "2":
        inventario.sort(key=lambda x: x["precio"])
    else:
        print("Opción no válida.")
        return

    # Set para mostrar categorías sin repetir
    categorias = set()

    for producto in inventario:
        categorias.add(producto["categoria"])

    print("\nCategorías:", ", ".join(categorias))

    print("\n--- INVENTARIO ---")
    print(
        f"{'CODIGO':<8}"
        f"{'NOMBRE':<25}"
        f"{'PRECIO':<10}"
        f"{'STOCK':<8}"
        f"{'CATEGORIA':<15}"
    )

    for producto in inventario:

        alerta = ""

        # Regla del proyecto: alerta de stock mínimo
        if producto["stock"] <= 3:
            alerta = " ¡STOCK BAJO!"

        print(
            f"{producto['codigo']:<8}"
            f"{producto['nombre']:<25}"
            f"Q{producto['precio']:<9.2f}"
            f"{producto['stock']:<8}"
            f"{producto['categoria']:<15}"
            f"{alerta}"
        )


def mostrar_reporte_ventas():
    """Muestra el reporte de las ventas realizadas."""

    if len(ventas) == 0:
        print("\nNo hay ventas registradas.")
        return

    print("\n--- REPORTE DE VENTAS ---")

    print(
        f"{'FECHA':<12}"
        f"{'CODIGO':<8}"
        f"{'PRODUCTO':<25}"
        f"{'CANT.':<8}"
        f"{'TOTAL':<10}"
    )

    total_dia = 0

    for venta in ventas:

        print(
            f"{venta[0]:<12}"
            f"{venta[1]:<8}"
            f"{venta[2]:<25}"
            f"{venta[3]:<8}"
            f"Q{venta[4]:<9.2f}"
        )

        total_dia += venta[4]

    print(f"\nTOTAL DEL DÍA: Q{total_dia:.2f}")