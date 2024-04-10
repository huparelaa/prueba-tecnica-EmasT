from models import MaterialFactory, ProductFactory, create_dummy_data

def main():
    print("Bienvenido a la bodega de productos E+T")
    material_factory = MaterialFactory()
    product_factory = ProductFactory()

    material_factory, product_factory = create_dummy_data()

    while True:
        print("1. Crear material")
        print("2. Crear producto")
        print("3. Ver materiales disponibles")
        print("4. Ver productos")
        print("5. Editar material")
        print("6. Editar producto")
        print("7. Salir")

        val = input("\033[92mIngrese el numero de la opcion que desea realizar: \033[0m")
        
        if val == "1":
            name = input("Ingrese el nombre del material: ")
            code = input("Ingrese el codigo del material: ")
            value = int(input("Ingrese el valor del material: "))
            quantity = int(input("Ingrese la cantidad del material: "))
            material_factory.create_material(name, code, value, quantity)
        elif val == "2":
            material_factory.get_available_materials()
            
            name = input("Ingrese el nombre del producto: ")
            code = input("Ingrese el codigo del producto: ")
            materials = []
            while True:
                material_factory.get_available_materials()
                material_code = input("Ingrese el codigo del material que desea agregar al producto: ")
                materials.append(material_factory.get_material(material_code))
                material_factory.use_material(material_code, 1)
                if input("Desea agregar otro material? (y/n): ") == "n":
                    break
            product_factory.create_product(name, code, materials)
        elif val == "3":
            material_factory.get_available_materials()
        elif val == "4":
            product_factory.get_products()

        elif val == "5":
            material_factory.get_available_materials()
            code = input("Ingrese el codigo del material que desea editar: ")
            quantity = int(input("Ingrese la nueva cantidad del material: "))
            if quantity < 0:
                print("La cantidad no puede ser negativa")
                continue
            material_factory.materials[code].quantity = quantity
        elif val == "6":
            product_factory.get_products()
            code = input("Ingrese el codigo del producto que desea editar: ")
            product = product_factory.get_product(code)
            print(product)
            print("1. Agregar material")
            print("2. Eliminar material")
            val = input("Ingrese el numero de la opcion que desea realizar: ")
            if val == "1":
                material_factory.get_available_materials()
                material_code = input("Ingrese el codigo del material que desea agregar al producto: ")
                product.materials.append(material_factory.get_material(material_code))
                material_factory.use_material(material_code, 1)
            elif val == "2":
                material_factory.get_available_materials()
                material_code = input("Ingrese el codigo del material que desea eliminar del producto: ")
                material_factory.materials[material_code].quantity += 1
                product.materials = [material for material in product.materials if material.code != material_code]
            else:
                print("Opcion invalida")
        elif val == "7":
            break
        else:
            print("Opcion invalida")
        print("\n")

main()

