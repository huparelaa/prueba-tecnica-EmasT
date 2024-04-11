class Shape:
    def area(self):
        pass

class Circulo(Shape):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

    def __str__(self):
        return f"Circulo de radio {self.radio}"
    
class Cuadrado(Shape):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado de lado {self.lado}"

class Triangulo(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        return f"Triangulo de base {self.base} y altura {self.altura}"
    
class Rectangulo(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"

figuras = ["circulo", "cuadrado", "triangulo", "rectangulo"]


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
    figura_seleccionada = list(figuras)[int(val) - 1]

    if figura_seleccionada in figuras:
        if val == "circulo":
            radio = float(input("Ingrese el radio del circulo: "))
            figura = Circulo(radio)
        elif val == "cuadrado":
            lado = float(input("Ingrese el lado del cuadrado: "))
            figura = Cuadrado(lado)
        elif val == "triangulo":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            figura = Triangulo(base, altura)
        elif val == "rectangulo":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            figura = Rectangulo(base, altura)

        print(f"Area de la figura: {figura.area()}")
        print(f"Figura: {figura}")
        print("\n")
    else:
        print("Figura no disponible")
        print("\n")
    