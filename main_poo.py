
# ==========================================
# PROYECTO FINAL
# SISTEMA DE INVENTARIO Y VENTAS CON POO
# ARCHIVO: main_poo.py
# ==========================================

from inventario.modelos import Producto
from inventario.ventas import GestorVentas
from inventario.repositorio import RepositorioCSV
from inventario.reglas import AlertaStock
from inventario.excepciones import (
    ProductoDuplicadoError,
    ProductoNoEncontradoError,
    StockInsuficienteError
)


# ==========================================
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# INTEGRACION DE CLASES
# ==========================================

def mostrar_productos(productos, regla):

    if not productos:
        print("No hay productos para mostrar.")
        return

    for producto in productos:

        alerta = regla.aplicar(producto)

        print(
            f"{producto.codigo} | "
            f"{producto.nombre} | "
            f"Q{producto.precio:.2f} | "
            f"Stock: {producto.stock} | "
            f"{producto.categoria} {alerta}"
        )


# ==========================================
# MENU PRINCIPAL
# ==========================================

def main():

    repositorio = RepositorioCSV("inventario.csv")

    try:
        inventario = repositorio.cargar()

    except (ValueError, OSError) as error:
        print("Error al cargar inventario:", error)
        return

    gestor = GestorVentas(inventario, "bitacora.txt")
    regla = AlertaStock(3)

    while True:

        print("\n========== MENU PRINCIPAL ==========")
        print("1. Ver inventario")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Registrar venta")
        print("5. Reporte de ventas")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opcion: ").strip()

        try:

            # ==================================
            # OPCION 1: VER INVENTARIO
            # ==================================

            if opcion == "1":

                criterio = input(
                    "Ordenar por nombre o precio: "
                ).strip().lower()

                productos = inventario.ordenar(criterio)

                mostrar_productos(productos, regla)

            # ==================================
            # OPCION 2: BUSCAR PRODUCTO
            # ==================================

            elif opcion == "2":

                texto = input(
                    "Ingrese codigo o nombre: "
                )

                encontrados = inventario.buscar(texto)

                mostrar_productos(encontrados, regla)

            # ==================================
            # OPCION 3: AGREGAR PRODUCTO
            # ==================================

            elif opcion == "3":

                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: Q"))
                stock = int(input("Stock: "))
                categoria = input("Categoria: ")

                producto = Producto(
                    codigo,
                    nombre,
                    precio,
                    stock,
                    categoria
                )

                inventario.agregar(producto)

                print("Producto agregado correctamente.")

            # ==================================
            # OPCION 4: REGISTRAR VENTA
            # ==================================

            elif opcion == "4":

                codigo = input("Codigo del producto: ")
                cantidad = int(input("Cantidad: "))

                venta = gestor.registrar_venta(
                    codigo,
                    cantidad
                )

                print("Venta registrada:", venta)

                producto = inventario.obtener(codigo)

                alerta = regla.aplicar(producto)

                if alerta:
                    print(alerta)

            # ==================================
            # OPCION 5: REPORTE DE VENTAS
            # ==================================

            elif opcion == "5":

                ventas = gestor.reporte_ventas()

                if not ventas:
                    print("No hay ventas registradas.")

                for venta in ventas:
                    print(venta)

                print(
                    f"Total vendido: "
                    f"Q{gestor.total_ventas():.2f}"
                )

            # ==================================
            # OPCION 6: GUARDAR Y SALIR
            # TEMA: PERSISTENCIA DE DATOS
            # ==================================

            elif opcion == "6":

                repositorio.guardar(inventario)

                gestor.guardar_historial()

                print("Inventario guardado correctamente.")
                print("Historial de ventas guardado.")
                print("Gracias por utilizar el sistema.")

                break

            else:
                print("Opcion no valida.")

        # ======================================
        # TEMA: MANEJO DE EXCEPCIONES
        # ======================================

        except (
            ProductoDuplicadoError,
            ProductoNoEncontradoError,
            StockInsuficienteError,
            ValueError,
            TypeError,
            OSError
        ) as error:

            print("Error:", error)


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()
