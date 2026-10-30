
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: inventario.py
# ==========================================

from .modelos import Producto


# ==========================================
# 3. CLASE INVENTARIO
# TEMA: COMPOSICION Y COLECCIONES
# DIAGRAMA UML: CLASE INVENTARIO
# ==========================================

class Inventario:
    """Administra los productos del inventario."""

    # TEMA: CONSTRUCTOR
    def __init__(self):
        # Diccionario para guardar productos
        self._productos = {}

    # ======================================
    # TEMA: AGREGAR PRODUCTO
    # DIAGRAMA UML: METODO AGREGAR
    # ======================================

    def agregar(self, producto):
        """Agrega un producto al inventario."""

        if producto.codigo in self._productos:
            raise ValueError("El codigo ya existe.")

        self._productos[producto.codigo] = producto

    # ======================================
    # TEMA: BUSCAR PRODUCTO
    # DIAGRAMA UML: METODO BUSCAR
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
    # DIAGRAMA UML: METODO OBTENER
    # ======================================

    def obtener(self, codigo):
        """Devuelve un producto por su codigo."""

        codigo = codigo.strip().upper()

        if codigo not in self._productos:
            raise ValueError("Producto no encontrado.")

        return self._productos[codigo]

    # ======================================
    # TEMA: ORDENAR INVENTARIO
    # DIAGRAMA UML: METODO ORDENAR
    # ======================================

    def ordenar(self, criterio):
        """Ordena productos por nombre o precio."""

        productos = list(self._productos.values())

        if criterio == "nombre":
            return sorted(productos, key=lambda p: p.nombre)

        if criterio == "precio":
            return sorted(productos, key=lambda p: p.precio)

        raise ValueError("Criterio no valido.")

    # ======================================
    # TEMA: SET DE CATEGORIAS
    # DIAGRAMA UML: METODO CATEGORIAS
    # ======================================

    def categorias(self):
        """Devuelve categorias sin repetir."""

        return {p.categoria for p in self._productos.values()}

    # ======================================
    # TEMA: METODOS ESPECIALES
    # DIAGRAMA UML: CLASE INVENTARIO
    # ======================================

    def __len__(self):
        """Devuelve la cantidad de productos."""
        return len(self._productos)

    def __contains__(self, codigo):
        """Comprueba si existe un codigo."""
        return codigo in self._productos

    def __iter__(self):
        """Permite recorrer los productos."""
        return iter(self._productos.values())
