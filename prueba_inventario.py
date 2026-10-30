
# ==========================================
# PRUEBA DEL SISTEMA DE INVENTARIO
# ==========================================

from inventario.inventario import Inventario
from inventario.modelos import Producto
from inventario.excepciones import ProductoDuplicadoError

# Crear inventario
inventario = Inventario()

# Crear producto
producto = Producto(
    "A0001",
    "Leche",
    12.50,
    9,
    "Lacteos"
)

# Agregar producto
inventario.agregar(producto)

# Mostrar resultado
print("Producto agregado:", inventario.obtener("A0001"))
print("Cantidad de productos:", len(inventario))

# Probar excepcion personalizada
try:
    inventario.agregar(producto)
except ProductoDuplicadoError:
    print("Excepcion personalizada funcionando")
