print("=== AGENDA DE TURNOS ===")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ").strip()

while not operador.isalpha():
    print("Error: ingrese solamente letras.")
    operador = input("Nombre del operador: ").strip()


opcion = ""

while opcion != "5":

    print("\n=== MENÚ ===")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida.")
        opcion = input("Opción: ")

    if opcion == "1":

        dia = input("Día (1 = Lunes / 2 = Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1 = Lunes / 2 = Martes): ")

        paciente = input("Nombre del paciente: ").strip()

        while not paciente.isalpha():
            print("Error: ingrese solamente letras.")
            paciente = input("Nombre del paciente: ").strip()


        if dia == "1":

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:

                print("Error: el paciente ya tiene un turno.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado.")

            else:
                print("No hay turnos disponibles para el lunes.")


        elif dia == "2":

            if paciente == martes1 or paciente == martes2 or paciente == martes3:

                print("Error: el paciente ya tiene un turno.")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado.")

            else:
                print("No hay turnos disponibles para el martes.")


    elif opcion == "2":

        dia = input("Día (1 = Lunes / 2 = Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1 = Lunes / 2 = Martes): ")

        paciente = input("Nombre del paciente: ").strip()

        while not paciente.isalpha():
            print("Error: ingrese solamente letras.")
            paciente = input("Nombre del paciente: ").strip()

        encontrado = False

        if dia == "1":

            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True

            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True

            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True

            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        elif dia == "2":

            if martes1 == paciente:
                martes1 = ""
                encontrado = True

            elif martes2 == paciente:
                martes2 = ""
                encontrado = True

            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontró un turno con ese nombre.")


    elif opcion == "3":

        dia = input("Día (1 = Lunes / 2 = Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1 = Lunes / 2 = Martes): ")

        if dia == "1":

            print("\n=== AGENDA LUNES ===")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        else:

            print("\n=== AGENDA MARTES ===")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)


    elif opcion == "4":

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1


        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\n=== RESUMEN GENERAL ===")
        print("Lunes - Ocupados:", ocupados_lunes)
        print("Lunes - Disponibles:", disponibles_lunes)

        print("Martes - Ocupados:", ocupados_martes)
        print("Martes - Disponibles:", disponibles_martes)

        if ocupados_lunes > ocupados_martes:
            print("El lunes tiene más turnos ocupados.")

        elif ocupados_martes > ocupados_lunes:
            print("El martes tiene más turnos ocupados.")

        else:
            print("Hay empate entre lunes y martes.")


    elif opcion == "5":

        print("Sistema cerrado.")