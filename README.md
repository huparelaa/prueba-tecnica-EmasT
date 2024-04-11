# Prueba técnica EmasT
Solución a prueba técnica de EmasT utilizando patrones de diseño como el uso de factorías para la instanciación de objetos en python así como de utilización de herencia.

## Shape.py
> [!TIP]
> Puede correr este programa con el comando `python shape.py`

En este programa se puede evidenciar el uso de la herencia para la creación de objetos, permitiéndones de esta manera abstraer correctamente la creación de figuras, las cuales heredan de la clase Shape, garantizándonos de esta manera que aquellas instancias que creemos cumplan con ciertas reglas que definimos para la creación de figuras, como que una figura debe tener un método para calcular el área de la figura.

### Extensibilidad
Este código es fácilmente extensible ya que bastaría con crear la clase con sus métodos tanto constructor como de obtención de área para añadirlo a la lista de figuras disponibles aquí:
```py
figuras = ["circulo", "cuadrado", "triangulo", "rectangulo"]
```
Entonces si decidimos añadir por ejemplo la figura "pentágono" con crear su constructor y el método para calcular el área ya podría ser utilizada en el flujo principal del programa.
Manteniendo así el principio open-closed que hace que nuestro código sea extensible para cambios y cerrado a modificaciones, ya que no tenemos que interactuar con las instancias de figuras ya creadas para añadir nuevas.

## Sistema de administración de materiales y productos
> [!TIP]
> Puede correr este programa con el comando `python products.py`

En esta propuesta de solución se sigue el patrón de diseño Factory para la creación de instancias de objetos, en este caso Material y Product, lo cual facilita en gran medida la implementación de nuevas funcionalidades gracias a las virtudes de la POO, además de que ayuda a la mantenibilidad del código, acompañado de múltiples funciones que facilitan la interacción del usuario con el sistema CLI.

> [!NOTE]
> En el archivo `models.py` se encuentra una función create_dummy_data() la cual iniciará el programa creando algunos materiales y productos, se puede comentar la línea 8 del `products.py` para empezar con el programa desde 0.
> ```py
> material_factory, product_factory = create_dummy_data()
> ```


