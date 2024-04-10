class Material:
    def __init__(self, name, code, value, quantity):
        self.name = name
        self.code = code
        self.value = value
        self.quantity = quantity

class Product:
    def __init__(self, name, code, materials: list):
        self.name = name
        self.code = code
        self.materials = materials

    def total_cost(self):
        return sum(material.value * material.quantity for material in self.materials)
    
    def __str__(self):
        return f"Producto {self.name} con codigo {self.code} y costo total {self.total_cost()}"
    
class ProductFactory:
    def __init__(self):
        self.products = {}
        
    def create_product(self, name, code, materials: list):
        self.products[code] = Product(name, code, materials)
        print(f"Producto {name} creado con exito")
        
    def get_product(self, code):
        if code not in self.products:
            raise ValueError("Producto no encontrado")
        return self.products[code]
    
    def get_products(self):
        print("Productos disponibles:")
        for product in self.products.values():
            print(product)
    
    def __str__(self):
        return f"Productos: {self.products}"
    
class MaterialFactory:
    def __init__(self):
        self.materials = {} 
        
    def create_material(self, name, code, value, quantity):
        self.materials[code] = Material(name, code, value, quantity)
        
    def get_material(self, code):
        return self.materials[code]
    
    def get_available_materials(self):
        print("Materiales disponibles:")
        for material in self.materials.values():
            print(f"Hay {material.quantity} unidades de {material.name} con codigo {material.code}")

    def use_material(self, code, quantity):
        if code not in self.materials:
            raise ValueError("Material no encontrado")
        if quantity > self.materials[code].quantity:
            raise ValueError("No hay suficiente material")
        self.materials[code].quantity -= quantity

    def __str__(self):
        return f"Materiales: {self.materials}"

def create_dummy_data():
    material_factory = MaterialFactory()
    product_factory = ProductFactory()

    material1 = Material("Madera", "MAD", 100, 10)
    material2 = Material("Metal", "MET", 200, 10)
    material3 = Material("Plastico", "PLA", 50, 10)

    material_factory.create_material(material1.name, material1.code, material1.value, material1.quantity)

    material_factory.create_material(material2.name, material2.code, material2.value, material2.quantity)

    material_factory.create_material(material3.name, material3.code, material3.value, material3.quantity)

    product1 = Product("Mesa", "MES", [material1, material2])

    product_factory.create_product(product1.name, product1.code, product1.materials)

    return material_factory, product_factory
