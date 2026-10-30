
# ==========================================
# PRUEBA DE PERSISTENCIA DEL INVENTARIO
# ==========================================

from pathlib import Path
from tempfile import TemporaryDirectory

from inventario.modelos import Producto
from inventario.inventario import Inventario
from inventario.repositorio import RepositorioCSV

# Usar un archivo temporal para no modificar
# el inventario.csv original del proyecto.

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "inventario_prueba.csv"

    inventario = Inventario()

    producto = Producto(
        "A0001", "Leche", 12.50, 9, "Lacteos"
    )

    inventario.agregar(producto)

    repositorio = RepositorioCSV(ruta)

    # Guardar los productos
    repositorio.guardar(inventario)
    print("Inventario guardado correctamente")

    # Recuperar los productos
    inventario_cargado = repositorio.cargar()

    print("Productos recuperados:", len(inventario_cargado))
    print("Producto:", inventario_cargado.obtener("A0001"))
