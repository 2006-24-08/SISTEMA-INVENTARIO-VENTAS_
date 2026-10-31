
# ==========================================
# PROYECTO FINAL
# SISTEMA DE INVENTARIO Y VENTAS CON POO
# ARCHIVO: prueba_polimorfismo.py
# ==========================================

from inventario.modelos import Producto

from inventario.reglas import (
    ReglaNegocio,
    SinAlerta,
    AlertaStock
)


# ==========================================
# TEMA: HERENCIA
# TEMA: CLASES ABSTRACTAS
# TEMA: POLIMORFISMO
# ==========================================

def probar_polimorfismo():

    print("===== PRUEBA DE POLIMORFISMO =====")

    # ======================================
    # CREACION DE OBJETO
    # ======================================

    producto = Producto(
        "A0001",
        "Leche Entera 1L",
        12.50,
        2,
        "Lacteos"
    )

    # ======================================
    # POLIMORFISMO
    # ======================================
    # Diferentes clases utilizan el mismo
    # metodo aplicar(), pero cada una
    # produce un resultado diferente.

    reglas = [
        SinAlerta(),
        AlertaStock(3)
    ]

    for regla in reglas:

        resultado = regla.aplicar(producto)

        print("\nClase:", type(regla).__name__)
        print("Producto:", producto.nombre)
        print("Stock:", producto.stock)

        if resultado:
            print("Resultado:", resultado)
        else:
            print("Resultado: Sin alerta")

    # ======================================
    # COMPROBACION DE HERENCIA
    # ======================================

    assert all(
        isinstance(regla, ReglaNegocio)
        for regla in reglas
    )

    # ======================================
    # COMPROBACION DE POLIMORFISMO
    # ======================================

    assert SinAlerta().aplicar(producto) == ""

    assert AlertaStock(3).aplicar(producto) == "¡STOCK BAJO!"

    print(
        "\nPRUEBA EXITOSA: polimorfismo funcionando."
    )


# ==========================================
# EJECUCION DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    probar_polimorfismo()
