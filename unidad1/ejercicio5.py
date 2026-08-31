print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ").strip()

while not nombre.isalpha():

    print("Error: Solo se permiten letras.")

    nombre = input("Nombre del Gladiador: ").strip()


vida_jugador = 100
vida_enemigo = 100
pociones = 3

dano_base = 15
dano_enemigo = 12

turno_gladiador = True


print("\n=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador == True:

        print("\n=== NUEVO TURNO ===")

        print(
            f"{nombre} (HP: {vida_jugador}) "
            f"vs Enemigo (HP: {vida_enemigo}) "
            f"| Pociones: {pociones}"
        )

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit():

            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        while int(opcion) < 1 or int(opcion) > 3:

            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")


        opcion = int(opcion)


        if opcion == 1:

            dano_final = dano_base

            if vida_enemigo < 20:

                dano_final = dano_base * 1.5
                print("¡GOLPE CRÍTICO!")

            vida_enemigo -= dano_final

            print(
                f"¡Atacaste al enemigo por "
                f"{dano_final} puntos de daño!"
            )


        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):

                vida_enemigo -= 5

                print(
                    "> Golpe conectado por 5 de daño"
                )


        elif opcion == 3:

            if pociones > 0:

                vida_jugador += 30
                pociones -= 1

                print("¡Usaste una poción y recuperaste 30 HP!")

            else:

                print("¡No quedan pociones!")


        turno_gladiador = False


    if vida_enemigo > 0 and turno_gladiador == False:

        vida_jugador -= dano_enemigo

        print(
            f">> ¡El enemigo contraataca por "
            f"{dano_enemigo} puntos!"
        )

        turno_gladiador = True


print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:

    print(
        f"¡VICTORIA! {nombre} ha ganado la batalla."
    )

else:

    print("DERROTA. Has caído en combate.")