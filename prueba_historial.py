
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: prueba_historial.py
# ==========================================

from pathlib import Path
from tempfile import TemporaryDirectory

from inventario.modelos import Producto
from inventario.inventario import Inventario
from inventario.ventas import GestorVentas


# ==========================================
# PRUEBA DE PERSISTENCIA DE VENTAS
# ==========================================

def probar_historial():

    # Crear carpeta temporal para las pruebas
    with TemporaryDirectory() as carpeta:

        ruta = Path(carpeta) / "bitacora_prueba.txt"

        # Crear inventario independiente
        inventario = Inventario()

        producto = Producto(
            "A0001",
            "Leche Entera 1L",
            12.50,
            9,
            "Lacteos"
        )

        inventario.agregar(producto)

        # Crear gestor con archivo temporal
        gestor = GestorVentas(inventario, ruta)

        # Registrar una venta de prueba
        venta = gestor.registrar_venta("A0001", 2)

        print("Venta registrada:", venta)
        print("Stock restante:", producto.stock)

        # Guardar el historial
        gestor.guardar_historial()

        # Comprobar que el archivo existe
        if ruta.exists():

            contenido = ruta.read_text(encoding="utf-8")

            print("\nHISTORIAL GUARDADO:")
            print(contenido)

            assert "A0001" in contenido
            assert "Q25.00" in contenido

            print("PRUEBA EXITOSA: historial guardado.")

        else:
            print("ERROR: No se creo el archivo.")


# ==========================================
# EJECUTAR PRUEBA
# ==========================================

if __name__ == "__main__":
    probar_historial()
