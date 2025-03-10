# vista.py

class Vista:
    @staticmethod
    def mostrar_menu():
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar Contacto")
        print("2. Mostrar Contactos")
        print("3. Buscar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")

    @staticmethod
    def obtener_opcion():
        return input("Seleccione una opción: ")

    @staticmethod
    def obtener_datos_contacto():
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        return nombre, telefono, email

    @staticmethod
    def mostrar_contacto(contacto):
        if contacto:
            print(contacto)
        else:
            print("Contacto no encontrado.")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
