import os

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    while nombre.strip() == '':
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del contacto: ")

    if nombre in agenda:
        print("Ya existe un contacto con ese nombre.")
    else:
        telefono = input("Ingrese el número de teléfono del contacto: ")
        if telefono.strip() != '':
            agenda[nombre] = telefono
            print("Contacto agregado correctamente.")
        else:
            print("El número de teléfono no puede estar vacío.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("El contacto no existe en la agenda.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print("El contacto no existe en la agenda.")

def mostrar_contactos(agenda):
    if len(agenda) > 0:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")

def guardar_agenda(agenda):
    with open("agenda.txt", "w") as archivo:
        for nombre, telefono in agenda.items():
            archivo.write(f"{nombre},{telefono}\n")

def cargar_agenda():
    agenda = {}
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(",")
                agenda[nombre] = telefono
    return agenda

def modificar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if nombre in agenda:
        telefono = input("Ingrese el nuevo número de teléfono: ")
        agenda[nombre] = telefono
        print("Contacto modificado correctamente.")
    else:
        print("El contacto no existe en la agenda.")

def main():
    agenda = cargar_agenda()

    while True:
        print("\n=== Agenda Telefónica ===")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Mostrar contactos")
        print("5. Modificar contacto")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            agregar_contacto(agenda)
            guardar_agenda(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
            guardar_agenda(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            mostrar_contactos(agenda)
        elif opcion == "5":
            modificar_contacto(agenda)
            guardar_agenda(agenda)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()