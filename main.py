from datetime import datetime

from operaciones import (
    cargar_inventario,
    guardar_inventario,
    mostrar_inventario,
    mostrar_reporte_ventas,
    registrar_log,
    ventas
)


# Cargar inventario al iniciar
inventario = cargar_inventario()


while True:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver inventario")
    print("2. Buscar producto")
    print("3. Agregar producto")
    print("4. Registrar venta")
    print("5. Reporte de ventas")
    print("6. Salir")

    opcion = input("Selecciona una opción: ").strip()


    # 1. Ver inventario
    if opcion == "1":

        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            mostrar_inventario(inventario)


    # 2. Buscar producto
    elif opcion == "2":

        buscar = input("Ingresa código o nombre: ").strip().lower()

        encontrado = False

        for producto in inventario:

            codigo = producto["codigo"].lower()
            nombre = producto["nombre"].lower()

            # Permite buscar por código o parte del nombre
            if buscar in codigo or buscar in nombre:

                print(
                    f"\nCódigo: {producto['codigo']}"
                    f"\nNombre: {producto['nombre']}"
                    f"\nPrecio: Q{producto['precio']:.2f}"
                    f"\nStock: {producto['stock']}"
                    f"\nCategoría: {producto['categoria']}"
                )

                encontrado = True

        if not encontrado:
            print("No se encontraron coincidencias.")


    # 3. Agregar producto
    elif opcion == "3":

        try:

            codigo = input("Código: ").strip().upper()

            # Validar formato: una letra + cuatro números
            if (
                len(codigo) != 5
                or not codigo[0].isalpha()
                or not codigo[1:].isdigit()
            ):
                print("Error: el código debe tener una letra y cuatro números.")
                continue

            # Revisar que el código no exista
            existe = False

            for producto in inventario:
                if producto["codigo"] == codigo:
                    existe = True

            if existe:
                print("Error: ese código ya existe.")
                continue

            nombre = input("Nombre: ").strip().title()

            precio = float(input("Precio: Q"))

            stock = int(input("Stock inicial: "))

            categoria = input("Categoría: ").strip().title()

            if precio <= 0:
                print("Error: el precio debe ser mayor que 0.")
                continue

            if stock < 0:
                print("Error: el stock no puede ser negativo.")
                continue

            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "categoria": categoria
            }

            inventario.append(producto)

            registrar_log(
                f"Producto agregado: {codigo} - {nombre}"
            )

            print("¡Producto agregado correctamente!")

        except ValueError:
            print("Error: debes ingresar números válidos.")


    # 4. Registrar venta
    elif opcion == "4":

        codigo = input("Código del producto a vender: ").strip().upper()

        encontrado = False

        for producto in inventario:

            if producto["codigo"] == codigo:

                encontrado = True

                try:

                    cantidad = int(
                        input(
                            f"Cantidad a vender de "
                            f"{producto['nombre']}: "
                        )
                    )

                    if cantidad <= 0:
                        print("La cantidad debe ser mayor que 0.")

                    elif cantidad > producto["stock"]:
                        print(
                            f"Stock insuficiente. "
                            f"Disponible: {producto['stock']}"
                        )

                    else:

                        # Restar la cantidad vendida
                        producto["stock"] -= cantidad

                        total = cantidad * producto["precio"]

                        fecha = datetime.now().strftime("%Y-%m-%d")

                        # Tupla para guardar la venta
                        venta = (
                            fecha,
                            producto["codigo"],
                            producto["nombre"],
                            cantidad,
                            total
                        )

                        ventas.append(venta)

                        registrar_log(
                            f"Venta: {cantidad}x "
                            f"{producto['nombre']} - Q{total:.2f}"
                        )

                        print(
                            f"¡Venta realizada correctamente!"
                            f" Total: Q{total:.2f}"
                        )

                except ValueError:
                    print("Error: la cantidad debe ser un número entero.")

                break

        if not encontrado:
            print("Producto no encontrado.")


    # 5. Reporte de ventas
    elif opcion == "5":

        mostrar_reporte_ventas()


    # 6. Salir
    elif opcion == "6":

        guardar_inventario(inventario)

        registrar_log("Inventario guardado. Programa cerrado.")

        print("\nInventario guardado correctamente.")
        print("¡Hasta luego!")

        break


    else:

        print("Opción no válida.")