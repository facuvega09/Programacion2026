class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print("\n--- MENÚ AGENDA ---")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        opcion = input("Seleccione una opción: ")
        return opcion

    def añadir(self):
        print("\n Nuevo Contacto")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print("Contacto guardado con éxito.")

    def listar(self):
        print("\n Lista de Contactos")
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for i, contacto in enumerate(self.contactos):
                print("ID:", i, "| Nombre:", contacto["nombre"], "| Tel:", contacto["telefono"], "| Email:", contacto["email"])

    def buscar(self):
        print("\n Buscar Contacto")
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre_buscar.lower():
                print("Resultado -> Nombre:", contacto["nombre"], "| Tel:", contacto["telefono"], "| Email:", contacto["email"])
                encontrado = True
        if not encontrado:
            print("No se encontró ningún contacto con ese nombre.")

    def editar(self):
        print("\n Editar Contacto")
        nombre_buscar = input("Ingrese el nombre del contacto que desea editar: ")
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre_buscar.lower():
                print("Datos actuales:", contacto)
                contacto["nombre"] = input("Nuevo nombre: ")
                contacto["telefono"] = input("Nuevo teléfono: ")
                contacto["email"] = input("Nuevo email: ")
                print("Contacto actualizado.")
                return
        print("No se encontró el contacto.")

agenda = Agenda()
opcion = ""

while opcion != "5":
    opcion = agenda.menu()

    if opcion == "1":
        agenda.añadir()
    elif opcion == "2":
        agenda.listar()
    elif opcion == "3":
        agenda.buscar()
    elif opcion == "4":
        agenda.editar()
    elif opcion == "5":
        print("Cerrando la agenda. ¡Hasta luego!")
    else:
        print("Opción no válida, intente de nuevo.")