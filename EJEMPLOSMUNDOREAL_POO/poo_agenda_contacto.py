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

# Continuación en agenda_contactos.py

class Agenda:
    def __init__(self):
        self.contactos = []             # Lista para almacenar objetos Contacto

    def agregar_contacto(self, contacto):
        # Añade un objeto Contacto a la lista
        self.contactos.append(contacto)

    def mostrar_todos(self):
        # Muestra todos los contactos almacenados
        return [contacto.mostrar_contacto() for contacto in self.contactos]

        # Continuación en agenda_contactos.py

    def buscar_por_nombre(self, nombre):
            # Busca contactos por nombre y devuelve una lista con coincidencias
            return [contacto for contacto in self.contactos if contacto.nombre == nombre]

# Código de prueba para usar las clases definidas

# Crear instancia de Agenda
mi_agenda = Agenda()

# Crear y agregar contactos
contacto1 = Contacto("Jessica Pesantez", "027304-513", "jess_12@example.com")
mi_agenda.agregar_contacto(contacto1)

contacto2 = Contacto("Alex Pesantez", "027304-056", "alexp15_20@example.com")
mi_agenda.agregar_contacto(contacto2)

# Mostrar todos los contactos
for info in mi_agenda.mostrar_todos():
    print(info)

# Buscar un contacto por nombre
resultados = mi_agenda.buscar_por_nombre("Jessica Pesantez")
for contacto in resultados:
    print("Contacto encontrado:", contacto.mostrar_contacto())
