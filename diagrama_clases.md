
classDiagram
    direction TB

    class Producto {
        -codigo
        -nombre
        -precio
        -stock
        -categoria
        +descontar_stock(cantidad)
        +__str__()
    }

    class Venta {
        +fecha
        +codigo
        +nombre
        +cantidad
        +total
    }

    class Inventario {
        -productos
        +agregar(producto)
        +buscar(criterio)
        +obtener(codigo)
        +ordenar(criterio)
        +categorias()
    }

    class GestorVentas {
        -inventario
        -ventas
        -archivo
        +registrar_venta(codigo, cantidad)
        +guardar_historial()
        +reporte_ventas()
        +total_ventas()
    }

    class RepositorioCSV {
        +cargar()
        +guardar(inventario)
    }

    class ReglaNegocio {
        <<abstract>>
        +aplicar(producto)*
    }

    class SinAlerta {
        +aplicar(producto)
    }

    class AlertaStock {
        -limite
        +aplicar(producto)
    }

    class ProductoDuplicadoError {
        <<exception>>
    }

    class ProductoNoEncontradoError {
        <<exception>>
    }

    class StockInsuficienteError {
        <<exception>>
    }

    ReglaNegocio <|-- SinAlerta
    ReglaNegocio <|-- AlertaStock
    Inventario o-- Producto
    GestorVentas --> Inventario
    GestorVentas --> Venta
    RepositorioCSV ..> Inventario
    GestorVentas ..> StockInsuficienteError
    Inventario ..> ProductoDuplicadoError
    Inventario ..> ProductoNoEncontradoError
      