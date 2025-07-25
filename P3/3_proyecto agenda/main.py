import agenda

def main():
    agenda_contacto = {}
    opcion = True
    while opcion:
        agenda.borrarPantalla()
        print("\t📒 .::MENÚ PRINCIPAL::. 📒\n")
        print("\t1️⃣.- Agregar contacto")
        print("\t2️⃣.- Mostrar contactos")
        print("\t3️⃣.- Buscar contacto")
        print("\t4️⃣.- Modificar contacto")
        print("\t5️⃣.- Eliminar contacto")
        print("\t6️⃣.- Salir")
        opcion = input("\nOpción seleccionada: ").strip()

        match opcion:
            case "1":
                agenda.agregarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "2":
                agenda.mostrarContactos(agenda_contacto)
                agenda.esperarTecla()
            case "3":
                agenda.buscarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "4":
                agenda.modificarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "5":
                agenda.eliminarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "6":
                agenda.borrarPantalla()
                print("🚪 .::Terminaste de usar el programa::. 🚪")
                opcion = False
            case _:
                print("⚠️ ::Opción no válida, vuelva a intentarlo:: ⚠️")
                agenda.esperarTecla()

if __name__ == "__main__":
    main()
