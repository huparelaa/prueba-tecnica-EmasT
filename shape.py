
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

    def __str__(self):
        return f"Circulo de radio {self.radio}"
    
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado de lado {self.lado}"
    
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    
    def __str__(self):
        return f"Triangulo de base {self.base} y altura {self.altura}"
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"
    
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
    
figuras = ShapeFactory().figuras.keys()

print("Figuras disponibles: ")

i = 1
for item in figuras:
    print(f"{i}. {item}")
    i+=1

while True:
    val = input("Ingrese el numero de la figura que desea crear: ")
    if val == "exit":
        break
    if val > str(len(figuras)) or val < "1":
        print("Figura no disponible")
        print("\n")
        continue
    val = list(figuras)[int(val) - 1]

    if val in figuras:
        factory = ShapeFactory()
        if val == "circulo":
            radio = float(input("Ingrese el radio del circulo: "))
            figura = factory.create_shape(val, radio)
        elif val == "cuadrado":
            lado = float(input("Ingrese el lado del cuadrado: "))
            figura = factory.create_shape(val, lado)
        elif val == "triangulo":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            figura = factory.create_shape(val, base, altura)
        elif val == "rectangulo":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            figura = factory.create_shape(val, base, altura)

        print(f"Area de la figura: {figura.area()}")
        print(f"Figura: {figura}")
        print("\n")
    else:
        print("Figura no disponible")
        print("\n")
    