class Agenda:
    def __init__(self):
        self.nombres = []
        self.telefonos = []
        self.gmails = [] 

    def menu(self):
        print("MENU")
        print("")
        print("Elija una de las siguientes opciones")
        print("")
        print("1) Añadir contacto")
        print("2) Lista de contactos")
        print("3) Buscar contacto")
        print("4) Editar contacto")
        print("5) Cerrar agenda")
        opcion = input("Elija una opcion: ")
        return opcion

    def añadir(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        gmail = input("Gmail: ") 
        
        self.nombres.append(nombre)
        self.telefonos.append(telefono)
        self.gmails.append(gmail)
        
    def listar(self):
        print("")
        print("CONTACTOS")
        cantidad = len(self.nombres)
        if cantidad == 0:
            print("No hay contactos")
        else:
            for i in range(cantidad):
                print(self.nombres[i], "-", self.telefonos[i], "-", self.gmails[i])
                print("")

    def buscar(self):
        nombre_buscar = input("ingrese el nombre a buscar: ")
        encontrado = 0

        for i in range(len(self.nombres)):
            if self.nombres[i] == nombre_buscar:
                print("Encontrado:", self.nombres[i], "- Telefono:", self.telefonos[i], "- gmail:", self.gmails[i])
                encontrado = 1

        if encontrado == 0:
            print("No se encontro el contacto.")

    def editar(self):
        nombre_buscar = input("Nombre del contacto a editar: ")
        encontrado = 0
        
        for i in range(len(self.nombres)):
            if self.nombres[i] == nombre_buscar:
                print("")
                self.nombres[i] = input("Nuevo nombre: ")
                self.telefonos[i] = input("Nuevo telefono: ")
                self.gmails[i] = input("Nuevo gmail: ")
                encontrado = 1
        
        if encontrado == 0:
            print("no existe.")

mi_agenda = Agenda()
opcion = ""

while opcion != "5":
    opcion = mi_agenda.menu()
    
    if opcion == "1":
        mi_agenda.añadir()
    elif opcion == "2":
        mi_agenda.listar()
    elif opcion == "3":
        mi_agenda.buscar()
    elif opcion == "4":
        mi_agenda.editar()
    elif opcion == "5":
        print("")
    else:
        print("Esa opcion no existe")