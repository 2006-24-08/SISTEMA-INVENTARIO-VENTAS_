
flowchart LR
    U["👤 Usuario"]

    subgraph S["Sistema de Inventario y Ventas"]
        A(["Consultar inventario"])
        B(["Buscar producto"])
        C(["Agregar producto"])
        D(["Registrar venta"])
        E(["Consultar reporte de ventas"])
        F(["Guardar información"])
    end

    U --- A
    U --- B
    U --- C
    U --- D
    U --- E
    U --- F
