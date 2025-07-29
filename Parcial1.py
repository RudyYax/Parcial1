empleados= {}
opcion = 0
print("Bienvenidos")
print("Parcial 1")
print("Bienvenidos")

while(opcion != 3):
    print("Menu Interactivo")
    print("1.- Registrar empleado")
    print("2.- Mostrar empleados")
    print("3.- Salir")
    opcion = int(input("Ingrese la opcion que deseea"))
    match(opcion):
        case 1:
            print("Ingresar datos de empleados")
            cantidad = int(input("Ingrese la cantidad de empleados que deseea guardar: "))
            for i in range(cantidad):

                print(f"Ingrese los datos del trabajador {i+1}")
                codigo = input("Ingrese el codigo del empleado")
                empleados[codigo] = {}
                empleados[codigo]["nombre"]= input("Ingresar nombre de empleado: ")
                empleados[codigo]["departamento"] = input("Ingresar departamento: ")
                empleados[codigo]["años"] = int(input("Ingrese los años de antiguedad"))
                empleados[codigo]["Contacto"] = {}
                empleados[codigo]['Contacto']["telefono"] = int(input("Ingrese el telefono del empleado: "))
                empleados[codigo]["Contacto"]["correo"] = input("Ingrese la correo del empleado: ")
                empleados[codigo]["Calificacion"] = {}
                empleados[codigo]['puntualidad'] = int(input("Ingrese la calificacion del empleado del 1 al 10"))
                empleados[codigo]['trabajo'] = int(input("Ingrese la calificacion del trabajo en equipo"))
                empleados[codigo]['productividad'] = int(input("Ingrese la calificacion de la productividad"))
                empleados[codigo]['observaciones'] = input("Ingrese alguna observacion general")
                print("Trabajador guardado exitosamente")

        case 2:
            print("Mostrar empleados")
            for codigo, empleado in empleados.items():
                print(f"\n Codigo del Empleado {[codigo]}")
                print(f"Nombre del Empleado {empleado['nombre']}")
                print(f"Departamento del Empleado {empleado['departamento']}")
                print(f"Años de antiguedad del empleado {empleado ['años']}")
                for codigo, calificacion in empleado["Calificacion"].items():
                    promedio = (calificacion["puntualidad"] + calificacion["trabajo"] + calificacion["productividad"]) / 3
                    print(f"\n Promedio {promedio}")
                    int(f"     Calificacion Puntualidad: {calificacion['puntualidad']}")
                    int(f"     Calificacion Trabajo: {calificacion['trabajo']}")
                    int(f"     Calificacion Productividad: {calificacion['productividad']}")








