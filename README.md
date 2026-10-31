# Sistema de Inventario y Ventas con Programación Orientada a Objetos

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de inventario y ventas utilizando Python y los principios de la Programación Orientada a Objetos (POO).

El sistema permite administrar productos, consultar existencias, registrar ventas y almacenar información mediante archivos CSV y TXT.

## Objetivo general

Desarrollar un sistema de inventario y ventas aplicando los conceptos fundamentales de la Programación Orientada a Objetos, con el propósito de organizar el código y facilitar su mantenimiento.

## Funcionalidades principales

- Visualizar los productos registrados.
- Buscar productos dentro del inventario.
- Agregar nuevos productos.
- Registrar ventas y actualizar las existencias.
- Consultar el reporte de ventas de la sesión.
- Guardar la información del inventario en un archivo CSV.
- Registrar el historial de ventas en un archivo TXT.
- Mostrar alertas cuando las existencias sean bajas.

## Conceptos de Programación Orientada a Objetos

**Clases y objetos:** Se utilizaron clases para representar productos, inventarios y ventas.

**Encapsulamiento:** Se implementaron atributos y propiedades para controlar el acceso y la modificación de datos.

**Herencia:** Las clases `SinAlerta` y `AlertaStock` heredan de la clase abstracta `ReglaNegocio`.

**Polimorfismo:** Las clases hijas implementan el método `aplicar()` con comportamientos diferentes.

**Abstracción:** Se utilizó una clase abstracta para establecer una estructura común para las reglas del sistema.

**Excepciones personalizadas:** Se implementaron excepciones para manejar productos duplicados, productos inexistentes y existencias insuficientes.

## Archivos principales

| Archivo | Función |
|---|---|
| `main_poo.py` | Ejecuta el menú principal del sistema. |
| `inventario/modelos.py` | Contiene las clases Producto y Venta. |
| `inventario/inventario.py` | Administra los productos. |
| `inventario/ventas.py` | Gestiona las ventas y su historial. |
| `inventario/repositorio.py` | Guarda y recupera los datos del inventario. |
| `inventario/reglas.py` | Contiene las reglas de negocio y demuestra herencia y polimorfismo. |
| `inventario/excepciones.py` | Define las excepciones personalizadas. |
| `inventario.csv` | Almacena los productos. |
| `bitacora.txt` | Guarda el historial de ventas. |
| `diagrama_clases.md` | Presenta el diagrama UML del sistema. |

## Ejecución del proyecto

1. Tener Python instalado.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal dentro de la carpeta principal.
4. Ejecutar el siguiente comando:

```powershell
python main_poo.py
```

## Pruebas del sistema

Se desarrollaron archivos de prueba para verificar el funcionamiento de los componentes:

- `prueba_inventario.py`
- `prueba_ventas.py`
- `prueba_repositorio.py`
- `prueba_historial.py`
- `prueba_polimorfismo.py`

Estas pruebas permiten comprobar el manejo del inventario, las ventas, la persistencia de datos y los conceptos de herencia y polimorfismo.

## Reflexión final

Durante el desarrollo de este proyecto pude comprender mejor la importancia de la Programación Orientada a Objetos y cómo permite organizar un programa mediante clases y métodos.

Uno de los principales aprendizajes fue transformar un sistema que inicialmente utilizaba funciones en una estructura orientada a objetos, separando las responsabilidades de cada componente.

También aprendí a utilizar la herencia, el polimorfismo, el encapsulamiento y las excepciones personalizadas para mejorar la organización y el funcionamiento del sistema.

Este proyecto me permitió fortalecer mis conocimientos de Python y comprender cómo aplicar los conceptos aprendidos en clase a un programa práctico.

## Control de versiones

El proyecto utiliza Git y GitHub para registrar los avances realizados durante su desarrollo.