# EjemplosMundoReal_POO/agenda_contactos.py

# Clase Contacto: representa un contacto con nombre, teléfono y email
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre            # Atributo nombre del contacto
        self.telefono = telefono        # Atributo teléfono
        self.email = email              # Atributo email

    def mostrar_contacto(self):
        # Método para mostrar la información del contacto
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
