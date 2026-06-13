"""
Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.
"""
ARCHIVO = "usuarios.txt"

from datetime import datetime

def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario:")

        if nombre == "":
            print("El nombre no puede estar vacío.")
            return

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                nombre_archivo, edad_archivo, fecha_hora_archivo = linea.strip().split(",")

                if nombre.lower() == nombre_archivo.lower():
                    print("El usuario ya se encuentra registrado")
                    return

        edad = int(input("Ingrese la edad del usuario:"))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return

        fecha_hora = datetime.now()  # Obtener la fecha y hora actual

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_hora}\n")

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
                nombre, edad, fecha_hora= linea.strip().split(",")
                print(f"Nombre: {nombre}, Edad: {edad}, Fecha y hora: {fecha_hora}")

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        
def validar_archivo():
    try:
        with open("usuarios_pruebas.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()    
        for linea in lineas:
            nombre, edad,  fecha_hora = linea.strip().split(",")
            edad = int(edad)
            
            if nombre == "":
                with open("usuarios_errores.txt", "a", encoding="utf-8") as archivo_errores:
                    archivo_errores.write(linea)
                continue
                    
            if edad < 0:
                with open("usuarios_errores.txt", "a", encoding="utf-8") as archivo_errores:
                    archivo_errores.write(linea)
                continue

            if edad > 120:
                with open("usuarios_errores.txt", "a", encoding="utf-8") as archivo_errores:
                    archivo_errores.write(linea)
                continue

            with open("usuarios_buenos.txt", "a", encoding="utf-8") as archivo_buenos:
                archivo_buenos.write(linea)

        print("Validación completada.")
                
    except FileNotFoundError:
        print("No se encontro el archivo de pruebas. ")
    except ValueError:
        print("La edad debe ser numérica.")
       
def menu():
    opcion = ""
    while opcion != "4":

        print("\n ==== USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Validar archivo")
        print("4. Salir") 
       

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            validar_archivo()
        elif opcion == "4":
           print("Programa finalizado.")
        else:
           print("Opción no válida. Intente nuevamente.")
menu()


