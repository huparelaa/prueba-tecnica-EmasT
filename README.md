# Prueba técnica EmasT
Solución a prueba técnica de EmasT utilizando patrones de diseño como el uso de factorías para la instanciación de objetos en python

## Shape.py
> [!TIP]
> Puede correr este programa con el comando `python shape.py`


En este programa se puede evidenciar el uso del patrón Factory para la creación de objetos, haciendo uso de la variable factory la cual genera todas las instancias que podamos necesitar de ciertas figuras.

### Extensibilidad
Este código es fácilmente extensible ya que bastaría con crear la clase con sus métodos tanto constructor como de obtención de área para añadirlo a la lista de shapeFactory:
```py
class ShapeFactory:
    def __init__(self):
        self.figuras = {
            "circulo": Circulo,
            "cuadrado": Cuadrado,
            "triangulo": Triangulo,
            "rectangulo": Rectangulo
        }

    def create_shape(self, tipo, *args):
        return self.figuras[tipo](*args)
```
Manteniendo así el principio Open-Close que hace que nuestro código sea extensible para cambios y cerrado a modificaciones, ya que no tenemos que interactuar con las instancias de figuras ya creadas para añadir nuevas.

## Sistema de administración de materiales y productos
> [!TIP]
> Puede correr este programa con el comando `python products.py`
De forma similar a como se realizó el punto de `shape.py` aquí también se sigue el patrón de diseño Factory para la creación de instancias de objetos, en este caso Material y Product, lo cual facilita en gran medida la implementación de nuevas funcionalidades gracias a las virtudes de la POO, además de que ayuda a la mantenibilidad del código.


