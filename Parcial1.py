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
                codigo = int(input("Ingrese el codigo del empleado"))
                nombre = input("Ingresar nombre de empleado: ")
                departamento = input("Ingresar departamento: ")
                años = int(input("Ingrese los años de antiguedad"))
                telefono = int(input("Ingrese el telefono del empleado: "))
                correo = input("Ingrese la correo del empleado: ")
                puntualidad = int(input("Ingrese la calificacion del empleado del 1 al 10"))
                trabajo = int(input("Ingrese la calificacion del trabajo en equipo"))
                productividad = int(input("Ingrese la calificacion de la productividad"))



