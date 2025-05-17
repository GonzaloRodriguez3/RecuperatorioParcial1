# Inicio del programa

# INICIAR dos listas vacías:
nombres = []
cantidades = []

# INICIAR variable bandera:
salir = True

# MIENTRAS salir HACER:
while salir:
    # MOSTRAR menú de opciones:
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

    # LEER opción del usuario
    opcion = input("Seleccione una opción (1-5): ").strip()

    # SI opción = "1" ENTONCES:
    if opcion == "1":
        # PEDIR nombre del producto → nombre
        nombre = input("Ingrese el nombre del producto: ").strip()

        # PEDIR cantidad en stock → cantidad
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad < 0:
                    print("⚠️ La cantidad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("⚠️ Ingrese un número entero válido.")

        # AGREGAR nombre a lista nombres
        nombres.append(nombre)

        # AGREGAR cantidad a lista cantidades
        cantidades.append(cantidad)

        # MOSTRAR "Producto agregado con éxito"
        print("✅ Producto agregado con éxito.")

    # SINO SI opción = "2" ENTONCES:
    elif opcion == "2":
        # MOSTRAR "Productos agotados:"
        print("\n=== Productos agotados ===")
        agotados = False

        # PARA i DESDE 0 HASTA longitud(nombres) - 1:
        for i in range(len(nombres)):
            # SI cantidades[i] = 0 ENTONCES: MOSTRAR nombres[i]
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True

        # SI agotados = falso ENTONCES:
        if not agotados:
            # MOSTRAR "No hay productos agotados"
            print("✅ No hay productos agotados.")

    # SINO SI opción = "3" ENTONCES:
    elif opcion == "3":
        # PEDIR nombre del producto → producto
        producto = input("Ingrese el nombre del producto a actualizar: ").strip()
        encontrado = False

        # SI producto EXISTE en nombres ENTONCES:
        for i in range(len(nombres)):
            if nombres[i].lower() == producto.lower():
                # index ← posición de producto en nombres
                index = i

                # PEDIR nueva cantidad → nueva_cantidad
                while True:
                    try:
                        nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombres[i]}': "))
                        if nueva_cantidad < 0:
                            print("⚠️ La cantidad no puede ser negativa.")
                        else:
                            break
                    except ValueError:
                        print("⚠️ Ingrese un número válido.")

                # cantidades[index] ← nueva_cantidad
                cantidades[index] = nueva_cantidad

                # MOSTRAR "Stock actualizado"
                print("✅ Stock actualizado.")
                encontrado = True
                break

        # SINO:
        if not encontrado:
            # MOSTRAR "Producto no encontrado"
            print("❌ Producto no encontrado.")

    # SINO SI opción = "4" ENTONCES:
    elif opcion == "4":
        # MOSTRAR "Listado de productos:"
        print("\n=== Listado de productos ===")
        # PARA i DESDE 0 HASTA longitud(nombres) - 1:
        for i in range(len(nombres)):
            # MOSTRAR nombres[i], cantidades[i]
            print(f"- {nombres[i]}: {cantidades[i]} unidades")

    # SINO SI opción = "5" ENTONCES:
    elif opcion == "5":
        # MOSTRAR "Gracias por usar el sistema"
        print("👋 Gracias por usar el sistema.")
        # salir = falso
        salir = False

    # SINO
