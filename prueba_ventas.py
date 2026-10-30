
# ==========================================
# PRUEBA DEL REGISTRO DE VENTAS
# ==========================================

from inventario.modelos import Producto
from inventario.inventario import Inventario
from inventario.ventas import GestorVentas
from inventario.excepciones import StockInsuficienteError

# Crear inventario
inventario = Inventario()

# Agregar producto
producto = Producto("A0001", "Leche", 12.50, 9, "Lacteos")
inventario.agregar(producto)

# Crear gestor de ventas
gestor = GestorVentas(inventario)

# Registrar venta de dos unidades
venta = gestor.registrar_venta("A0001", 2)

print("Venta registrada:", venta)
print("Stock restante:", producto.stock)
print("Total vendido: Q", gestor.total_ventas())

# Probar stock insuficiente
try:
    gestor.registrar_venta("A0001", 20)
except StockInsuficienteError:
    print("Excepcion de stock insuficiente funcionando")
