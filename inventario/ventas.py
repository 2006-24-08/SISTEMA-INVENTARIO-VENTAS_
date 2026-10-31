
# ==========================================
# SISTEMA DE INVENTARIO Y VENTAS
# ARCHIVO: inventario/ventas.py
# ==========================================

from datetime import datetime
from pathlib import Path

from .modelos import Venta
from .excepciones import StockInsuficienteError


# ==========================================
# CLASE: GESTORVENTAS
# POO: ENCAPSULAMIENTO Y COMPOSICION
# PERSISTENCIA: ARCHIVOS DE TEXTO
# ==========================================

class GestorVentas:

    def __init__(self, inventario, archivo="bitacora.txt"):
        self._inventario = inventario
        self._ventas = []
        self._archivo = Path(archivo)

    # REGISTRAR VENTA
    def registrar_venta(self, codigo, cantidad):

        producto = self._inventario.obtener(codigo)

        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if cantidad > producto.stock:
            raise StockInsuficienteError(
                "No hay suficientes unidades disponibles."
            )

        total = producto.precio * cantidad

        producto.descontar_stock(cantidad)

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        venta = Venta(
            fecha,
            producto.codigo,
            producto.nombre,
            cantidad,
            total
        )

        self._ventas.append(venta)
        return venta

    # GUARDAR HISTORIAL EN ARCHIVO TXT
    def guardar_historial(self):

        if not self._ventas:
            return

        with open(self._archivo, "a", encoding="utf-8") as archivo:

            for venta in self._ventas:
                archivo.write(
                    f"{venta.fecha} | "
                    f"{venta.codigo} | "
                    f"{venta.nombre} | "
                    f"Cantidad: {venta.cantidad} | "
                    f"Total: Q{venta.total:.2f}\n"
                )

        self._ventas.clear()

    # REPORTE DE VENTAS
    def reporte_ventas(self):
        return self._ventas.copy()

    # TOTAL VENDIDO
    def total_ventas(self):
        return sum(venta.total for venta in self._ventas)

    # METODO ESPECIAL
    def __len__(self):
        return len(self._ventas)
