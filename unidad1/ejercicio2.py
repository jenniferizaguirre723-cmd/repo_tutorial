print("=== ACCESO AL CAMPUS ===")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and acceso == False:

    print(f"\nIntento {intentos + 1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        intentos += 1
        print("Error: credenciales inválidas.")


if acceso == False:

    print("Cuenta bloqueada.")

else:

    opcion = ""

    while opcion != "4":

        print("\n=== MENÚ ===")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion_numero = int(opcion)

        while opcion_numero < 1 or opcion_numero > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

            opcion_numero = int(opcion)

        opcion = str(opcion_numero)

        if opcion == "1":

            print("Estado de inscripción: Inscripto")

        elif opcion == "2":

            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")

            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave modificada correctamente.")
            else:
                print("Error: las claves no coinciden.")

        elif opcion == "3":

            print("¡Seguí practicando, cada ejercicio te ayuda a mejorar!")

        elif opcion == "4":

            print("Sesión finalizada.")