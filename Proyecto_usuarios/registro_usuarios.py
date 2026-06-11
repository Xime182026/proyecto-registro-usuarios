ARCHIVO = "usuarios.txt"

def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario:")

        if nombre == "":
            print("El nombre no puede estar vacío.")
            return
        edad = int(input("Ingrese la edad del usuario:"))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad}\n")
        print("Usuario registrado exitosamente.")
    
    except ValueError:
        print("La edad debe de ser numérica")
    
    except PermissionError:
        print("No se tienen permisos para escribir en el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
            
    
def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return
            
            print("\nUsuarios registrados:")

            for linea in lineas:
                nombre, edad = linea.strip().split(",")
                print(f"Nombre: {nombre}, Edad: {edad}")

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

def menu():
    opcion = ""
    while opcion != "3":

        print("\n ==== USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

menu()


