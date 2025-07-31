propietarios = {}
while True:
    print("\n\n----------Control de autos----------\n1. Ingresar persona\n2. Mostrar todas las personas\n3. Estado de pago de una persona\n4. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":
            while True:
                try:
                    nit = int(input("Ingrese su NIT: "))
                    nombre = input("Ingrese su nombre completo: ")
                    telefono = int(input("Ingrese su telefono: "))
                    auto_cant =int(input("Ingrese la cantidad de autos que posee: "))

                    if len(str(nit))!=13:
                        print("El NIT debe tener 13 dígitos")
                    elif len(str(telefono)) != 8:
                        print("El número de teléfono debe tener 8 dígitos")
                    elif auto_cant<0:
                        print("La cantidad de autos debe ser positiva o 0")
                    else:
                        break
                except:
                    print("Ingrese una serie de números enteros")

            if auto_cant == 0:
                pass
            else:
                autos : {}
                for i in range(auto_cant):
                    print("-"*5 + f" AUTO {i+1} " + "-*5")
                    placa = input("Ingrese la placa: ")
                    marca = input("Ingrese la marca: ")
                    modelo = input("Ingrese el modelo: ")
                    while True:
                        ano = input("Ingrese el año: ")
                        if ano.isdigit():
                            ano = int(ano)
                            break
                        else:
                            print("Ingrese el año en números")

                    while True:
                        impuesto = input("¿Ya se ha pagado el impuesto del auto?: ").lower()
                        if impuesto == "si" or impuesto == "sí" or impuesto == "no":
                            break
                        else:
                            print("Ingrese SI o NO por favor")
                    autos[placa]= {
                        "marca": marca,
                        "modelo": modelo,
                        "ano": ano,
                        "impuesto": impuesto,
                    }

            propietarios[nit] = {
                "nombre": nombre,
                "telefono": telefono,
                "autos": autos
            }


        case "2":
            if not propietarios:
                print("No hay propietarios")
            else:
                for NIT, prop in propietarios.items():
                    print("\nNIT: " + NIT)
                    print("Nombre: " + prop["nombre"])
                    print("Telefono: " + prop["telefono"])
                    print("Autos:")
                    for placa, auto in prop["autos"].items():
                        print("Placa: " + placa)
                        print("Modelo: " + auto["modelo"])
                        print("año: " + auto["ano"])
                        print("¿Pagó el impuesto?: " + auto["impuesto"])


        case "3":
            if not propietarios:
                print("No hay propietarios")
            else:
                while True:
                    nit_search = input("Ingrese el NIT: ")
                    if nit_search.isdigit():
                        nit_search = int(nit_search)
                        if len(str(nit_search))!=13:
                            print("El NIT debe tener 13 números")
                        else:
                            break
                    else:
                        print("Ingrese solo números")

                if nit_search in propietarios.keys():
                    propietario = propietarios[nit_search]
                    pagado_cant = 0
                    nopagado_cant = 0
                    for placa, auto in prop["autos"].items():
                        if auto["impuesto"] == "si" or auto["impuesto"] == "sí":
                            pagado_cant += 1
                        else:
                            nopagado_cant += 1

                    print(f"Total de vehículos con impuesto pagado: {pagado_cant}")
                    print(f"Total de vehículos sin impuesto pagado: {nopagado_cant}")




        case "4":
            print("Saliendo...")
            break
        case _:
            print("Seleccione una opción válida")