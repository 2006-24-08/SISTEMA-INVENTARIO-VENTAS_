
from dataclasses import dataclass


# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: modelos.py
# ==========================================


# ==========================================
# 1. CLASE PRODUCTO
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# DIAGRAMA UML: CLASE PRODUCTO
# ==========================================

class Producto:
    """Representa un producto del inventario."""

    # TEMA: CONSTRUCTOR
    def __init__(self, codigo, nombre, precio, stock, categoria):
        self._codigo = ""
        self._nombre = nombre
        self._precio = 0
        self._stock = 0
        self._categoria = categoria

        self.codigo = codigo
        self.precio = precio
        self.stock = stock

    # ======================================
    # TEMA: ENCAPSULAMIENTO
    # DIAGRAMA UML: ATRIBUTOS DE PRODUCTO
    # ======================================

    @property
    def codigo(self):
        """Devuelve el codigo del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """Valida el formato del codigo."""
        valor = valor.strip().upper()

        if (len(valor) != 5 or
                not valor[0].isalpha() or
                not valor[1:].isdigit()):
            raise ValueError("Codigo invalido.")

        self._codigo = valor

    @property
    def precio(self):
        """Devuelve el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """Valida que el precio sea positivo."""
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = valor

    @property
    def stock(self):
        """Devuelve las unidades disponibles."""
        return self._stock

    @stock.setter
    def stock(self, valor):
        """Evita cantidades negativas."""
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    @property
    def nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    @property
    def categoria(self):
        """Devuelve la categoria del producto."""
        return self._categoria

    # ======================================
    # TEMA: METODOS DE LA CLASE PRODUCTO
    # DIAGRAMA UML: METODOS DE PRODUCTO
    # ======================================

    def descontar_stock(self, cantidad):
        """Descuenta unidades disponibles."""
        if cantidad <= 0:
            raise ValueError("Cantidad invalida.")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")

        self.stock -= cantidad

    # TEMA: METODO ESPECIAL
    def __str__(self):
        """Muestra informacion del producto."""
        return f"{self.codigo} - {self.nombre}"

    # TEMA: METODO ESPECIAL
    def __repr__(self):
        """Representacion del producto."""
        return f"Producto({self.codigo}, {self.nombre})"


# ==========================================
# 2. CLASE VENTA
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# DIAGRAMA UML: CLASE VENTA
# ==========================================

@dataclass(frozen=True)
class Venta:
    """Guarda los datos de una venta."""

    fecha: str
    codigo: str
    nombre: str
    cantidad: int
    total: float

    # ======================================
    # TEMA: METODO ESPECIAL
    # DIAGRAMA UML: METODO MOSTRAR
    # ======================================

    def __str__(self):
        """Muestra un resumen de la venta."""
        return f"{self.nombre}: {self.cantidad} unidades - Q{self.total:.2f}"
