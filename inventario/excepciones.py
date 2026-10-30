
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: excepciones.py
# ==========================================

# TEMA: EXCEPCIONES PERSONALIZADAS
# DIAGRAMA UML: CLASES DE EXCEPCIONES

# 1. PRODUCTO DUPLICADO
class ProductoDuplicadoError(Exception):
    """Se utiliza cuando el codigo ya existe."""
    pass


# 2. PRODUCTO NO ENCONTRADO
class ProductoNoEncontradoError(Exception):
    """Se utiliza cuando no existe un producto."""
    pass


# 3. STOCK INSUFICIENTE
class StockInsuficienteError(Exception):
    """Se utiliza cuando no hay suficientes unidades."""
    pass
