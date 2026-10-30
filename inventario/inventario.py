
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: inventario.py
# ==========================================

from .modelos import Producto

from .excepciones import (
    ProductoDuplicadoError,
    ProductoNoEncontradoError
)


# ==========================================
# 3. CLASE INVENTARIO
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# DIAGRAMA UML: CLASE INVENTARIO
# ==========================================

class Inventario:
    """Administra los productos del inventario."""

    # ======================================
    # TEMA: CONSTRUCTOR Y ENCAPSULAMIENTO
    # ======================================

    def __init__(self):
        # Diccionario para almacenar productos
        self._productos = {}

    # ======================================
    # TEMA: AGREGAR PRODUCTO
    # TEMA: EXCEPCIONES PERSONALIZADAS
    # ======================================

    def agregar(self, producto):
        """Agrega un producto al inventario."""

        if not isinstance(producto, Producto):
            raise TypeError("Debe ingresar un producto valido.")

        if producto.codigo in self._productos:
            raise ProductoDuplicadoError(
                "El codigo ya existe."
            )

        self._productos[producto.codigo] = producto

    # ======================================
    # TEMA: BUSCAR PRODUCTO
    # TEMA: LISTAS Y COLECCIONES
    # ======================================

    def buscar(self, texto):
        """Busca productos por codigo o nombre."""

        texto = texto.strip().lower()
        encontrados = []

        for producto in self._productos.values():

            if (texto in producto.codigo.lower()
                    or texto in producto.nombre.lower()):

                encontrados.append(producto)

        return encontrados

    # ======================================
    # TEMA: OBTENER PRODUCTO POR CODIGO
    # TEMA: EXCEPCIONES PERSONALIZADAS
    # ======================================

    def obtener(self, codigo):
        """Devuelve un producto por su codigo."""

        codigo = codigo.strip().upper()

        if codigo not in self._productos:
            raise ProductoNoEncontradoError(
                "Producto no encontrado."
            )

        return self._productos[codigo]

    # ======================================
    # TEMA: ORDENAR INVENTARIO
    # TEMA: COLECCIONES Y LAMBDA
    # ======================================

    def ordenar(self, criterio):
        """Ordena productos por nombre o precio."""

        productos = list(self._productos.values())

        if criterio == "nombre":
            return sorted(
                productos,
                key=lambda p: p.nombre.lower()
            )

        if criterio == "precio":
            return sorted(
                productos,
                key=lambda p: p.precio
            )

        raise ValueError("Criterio no valido.")

    # ======================================
    # TEMA: SET DE CATEGORIAS
    # ======================================

    def categorias(self):
        """Devuelve las categorias sin repetir."""

        return {
            producto.categoria
            for producto in self._productos.values()
        }

    # ======================================
    # TEMA: METODOS ESPECIALES
    # ======================================

    def __len__(self):
        """Devuelve la cantidad de productos."""
        return len(self._productos)

    def __contains__(self, codigo):
        """Comprueba si existe un codigo."""
        return codigo.strip().upper() in self._productos

    def __iter__(self):
        """Permite recorrer los productos."""
        return iter(self._productos.values())
