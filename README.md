# Prueba - Programación Avanzada en Python

## Descripción

Este proyecto consiste en crear una API en Python para gestionar campañas publicitarias. La API debe manejar diferentes tipos de anuncios y permitir la modificación de campañas y anuncios.

## Requisitos

1. **Clases y Atributos**:
   - **`anuncio.py`**: Define las clases `Anuncio`, `Video`, `Display`, y `Social`.
   - **`campaña.py`**: Define la clase `Campaña`.

2. **Excepciones**:
   - **`error.py`**: Define las excepciones personalizadas `LargoExcedidoError` y `SubTipoInvalidoError`.

3. **Script de Demostración**:
   - **`demo.py`**: Un script que crea una campaña, modifica sus atributos, y maneja errores.

## Archivos del Proyecto

- **`anuncio.py`**: Implementa la clase base `Anuncio` y sus subclases (`Video`, `Display`, `Social`).
- **`campaña.py`**: Implementa la clase `Campaña`.
- **`error.py`**: Define las excepciones `LargoExcedidoError` y `SubTipoInvalidoError`.
- **`demo.py`**: Ejemplo de uso que muestra cómo crear y modificar campañas.

## Reglas de Negocio

- **`Anuncio`**:
  - Dimensiones deben ser mayores a cero.
  - El `sub_tipo` debe ser válido según el tipo de anuncio.
  - Método estático `mostrar_formatos` muestra formatos y subtipos.

- **`Video`**:
  - Ancho y alto deben ser 1.
  - `duracion` debe ser mayor a cero.

- **`Display` y `Social`**:
  - Métodos para compresión y redimensionamiento deben mostrar mensajes específicos.

- **`Campaña`**:
  - Nombre no debe exceder 250 caracteres.
  - Getter para `anuncios`.
  - Método `__str__` muestra información sobre la campaña y anuncios.

## Cómo Ejecutar

1. Implementa las clases y métodos según las especificaciones.
2. Ejecuta `demo.py` para probar la funcionalidad.
3. Revisa `error.log` para cualquier error registrado.

## Entregables

1. Archivos de código (`anuncio.py`, `campaña.py`, `error.py`, `demo.py`).
2. Archivo `README.md`.