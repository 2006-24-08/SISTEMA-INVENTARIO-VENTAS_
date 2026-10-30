
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: ventas.py
# ==========================================

from datetime import datetime

from .modelos import Venta
from .excepciones import StockInsuficienteError


# ==========================================
# 7. CLASE GESTORVENTAS
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# DIAGRAMA UML: CLASE GESTORVENTAS
# ==========================================

class GestorVentas:
    """Administra las ventas del sistema."""

    # ======================================
    # TEMA: CONSTRUCTOR Y ENCAPSULAMIENTO
    # ======================================

    def __init__(self, inventario):
        self._inventario = inventario
        self._ventas = []

    # ======================================
    # TEMA: REGISTRAR VENTA
    # TEMA: EXCEPCIONES PERSONALIZADAS
    # ======================================

    def registrar_venta(self, codigo, cantidad):
        """Registra una venta y descuenta el stock."""

        producto = self._inventario.obtener(codigo)

        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser un numero entero positivo."
            )

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

    # ======================================
    # TEMA: REPORTE DE VENTAS
    # ======================================

    def reporte_ventas(self):
        """Devuelve las ventas registradas."""
        return self._ventas.copy()

    # ======================================
    # TEMA: CALCULAR TOTAL DE VENTAS
    # ======================================

    def total_ventas(self):
        """Calcula el dinero de las ventas."""
        return sum(venta.total for venta in self._ventas)

    # ======================================
    # TEMA: METODO ESPECIAL
    # ======================================

    def __len__(self):
        """Devuelve la cantidad de ventas."""
        return len(self._ventas)
