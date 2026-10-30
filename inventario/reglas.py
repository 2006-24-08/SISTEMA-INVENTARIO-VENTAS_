
# ==========================================
# PROYECTO FINAL - SISTEMA DE INVENTARIO
# ARCHIVO: reglas.py
# ==========================================

from abc import ABC, abstractmethod


# ==========================================
# 4. CLASE ABSTRACTA
# TEMA: ABSTRACCION
# DIAGRAMA UML: CLASE REGLANEGOCIO
# ==========================================

class ReglaNegocio(ABC):
    """Define una regla para revisar productos."""

    def __init__(self, limite=3):
        """Guarda el limite de stock."""
        self._limite = limite

    @abstractmethod
    def aplicar(self, producto):
        """Revisa un producto y devuelve un mensaje."""
        pass


# ==========================================
# 5. CLASE SIN ALERTA
# TEMA: HERENCIA
# DIAGRAMA UML: CLASE SINALERTA
# ==========================================

class SinAlerta(ReglaNegocio):
    """Regla que no genera advertencias."""

    def __init__(self):
        """Inicializa la regla."""
        super().__init__()

    def aplicar(self, producto):
        """Devuelve un mensaje vacio."""
        return ""


# ==========================================
# 6. CLASE ALERTA STOCK
# TEMA: HERENCIA Y POLIMORFISMO
# DIAGRAMA UML: CLASE ALERTASTOCK
# ==========================================

class AlertaStock(ReglaNegocio):
    """Genera una alerta cuando hay poco stock."""

    def __init__(self, limite=3):
        """Establece el limite de stock."""
        super().__init__(limite)

    def aplicar(self, producto):
        """Comprueba si el stock es bajo."""
        if producto.stock <= self._limite:
            return "¡STOCK BAJO!"
        return ""
