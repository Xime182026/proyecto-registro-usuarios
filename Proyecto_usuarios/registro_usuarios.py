"""
Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.
"""
from datetime import datetime

ARCHIVO = "usuarios.txt"
ARCHIVO_PRUEBAS = "usuarios_pruebas.txt"
ARCHIVO_BUENOS = "usuarios_buenos.txt"
ARCHIVO_ERRORES = "usuarios_errores.txt"


def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ")

        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            return

        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            lineas = []

        for linea in lineas:
            datos = linea.strip().split(",")

            if len(datos) < 3:
                continue

            nombre_archivo = datos[0]

            if nombre.lower() == nombre_archivo.lower():
                print("El usuario ya se encuentra registrado.")
                return

        edad = int(input("Ingrese la edad del usuario: "))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return

        if edad > 120:
            print("La edad no puede ser mayor a 120 años.")
            return

        fecha_hora = datetime.now()

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_hora}\n")

        print("Usuario registrado exitosamente.")

    except ValueError:
        print("La edad debe ser numérica.")

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
            datos = linea.strip().split(",")

            if len(datos) < 3:
                continue

            nombre = datos[0]
            edad = datos[1]
            fecha_hora = ",".join(datos[2:])

            print(f"Nombre: {nombre}, Edad: {edad}, Fecha y hora: {fecha_hora}")

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def validar_archivo():
    try:
        with open(ARCHIVO_PRUEBAS, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            try:
                nombre, edad, fecha_hora = linea.strip().split(",")

                edad = int(edad)

                if nombre == "" or edad < 0 or edad > 120:
                    with open(ARCHIVO_ERRORES, "a", encoding="utf-8") as archivo_errores:
                        archivo_errores.write(linea)
                else:
                    with open(ARCHIVO_BUENOS, "a", encoding="utf-8") as archivo_buenos:
                        archivo_buenos.write(linea)

            except Exception:
                with open(ARCHIVO_ERRORES, "a", encoding="utf-8") as archivo_errores:
                    archivo_errores.write(linea)

        print("Validación completada.")

    except FileNotFoundError:
        print("No se encontró el archivo de pruebas.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def menu():
    opcion = ""

    while opcion != "4":

        print("\n==== USUARIOS ====")
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
