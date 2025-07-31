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


        case "3":
            pass
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Seleccione una opción válida")