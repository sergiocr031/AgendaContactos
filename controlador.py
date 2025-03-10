# controlador.py

from modelo import Contacto, Agenda
from vista import Vista

class Controlador:
    def __init__(self):
        self.agenda = Agenda()
        self.vista = Vista()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == '1':
                nombre, telefono, email = self.vista.obtener_datos_contacto()
                contacto = Contacto(nombre, telefono, email)
                self.agenda.agregar_contacto(contacto)
                self.vista.mostrar_mensaje("Contacto agregado con éxito.")
            
            elif opcion == '2':
                contactos = self.agenda.listar_contactos()
                for contacto in contactos:
                    self.vista.mostrar_contacto(contacto)
            
            elif opcion == '3':
                nombre = input("Nombre a buscar: ")
                contacto = self.agenda.buscar_contacto(nombre)
                self.vista.mostrar_contacto(contacto)
            
            elif opcion == '4':
                nombre = input("Nombre a eliminar: ")
                if self.agenda.eliminar_contacto(nombre):
                    self.vista.mostrar_mensaje("Contacto eliminado.")
                else:
                    self.vista.mostrar_mensaje("Contacto no encontrado.")
            
            elif opcion == '5':
                self.vista.mostrar_mensaje("Saliendo...")
                break
            
            else:
                self.vista.mostrar_mensaje("Opción no válida.")
