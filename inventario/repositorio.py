
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: repositorio.py
# ==========================================

import csv
from pathlib import Path

from .modelos import Producto
from .inventario import Inventario


# ==========================================
# 8. CLASE REPOSITORIO CSV
# TEMA: PROGRAMACION ORIENTADA A OBJETOS
# TEMA: PERSISTENCIA DE DATOS
# DIAGRAMA UML: CLASE REPOSITORIOCSV
# ==========================================

class RepositorioCSV:
    """Guarda y carga productos en un archivo CSV."""

    # ======================================
    # TEMA: CONSTRUCTOR Y ENCAPSULAMIENTO
    # ======================================

    def __init__(self, archivo="inventario.csv"):
        self._archivo = Path(archivo)

    # ======================================
    # TEMA: CARGAR INVENTARIO
    # TEMA: MANEJO DE ARCHIVOS
    # ======================================

    def cargar(self):
        """Carga los productos desde el archivo CSV."""

        inventario = Inventario()

        if not self._archivo.exists():
            return inventario

        with open(
            self._archivo,
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as archivo:

            lector = csv.reader(archivo)

            for fila in lector:

                if not fila:
                    continue

                if len(fila) != 5:
                    raise ValueError(
                        "El archivo contiene una fila incorrecta."
                    )

                codigo, nombre, precio, stock, categoria = fila

                # Omitir el encabezado si existe
                if codigo.strip().lower() == "codigo":
                    continue

                producto = Producto(
                    codigo,
                    nombre,
                    float(precio),
                    int(stock),
                    categoria
                )

                inventario.agregar(producto)

        return inventario

    # ======================================
    # TEMA: GUARDAR INVENTARIO
    # TEMA: MANEJO DE ARCHIVOS
    # ======================================

    def guardar(self, inventario):
        """Guarda los productos y su encabezado en CSV."""

        with open(
            self._archivo,
            "w",
            encoding="utf-8-sig",
            newline=""
        ) as archivo:

            escritor = csv.writer(archivo)

            # Escribir los nombres de las columnas
            escritor.writerow([
                "codigo",
                "nombre",
                "precio",
                "stock",
                "categoria"
            ])

            # Guardar todos los productos
            for producto in inventario:

                escritor.writerow([
                    producto.codigo,
                    producto.nombre,
                    producto.precio,
                    producto.stock,
                    producto.categoria
                ])
