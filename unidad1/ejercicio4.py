print("=== ESCAPE ROOM: LA BÓVEDA ===")

nombre = input("Nombre del agente: ").strip()

while not nombre.isalpha():
    print("Error: ingrese solamente letras.")
    nombre = input("Nombre del agente: ").strip()


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0
bloqueado = False


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:

    print("\n========================")
    print("Agente:", nombre)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Código parcial:", codigo_parcial)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: opción inválida.")
        opcion = input("Opción: ")


    if opcion == "1":

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:

            print("¡La cerradura se trabó!")
            print("ALARMA ACTIVADA.")

            alarma = True
            forzar_seguidas = 0

        else:

            if energia < 40:

                riesgo = input("Riesgo de alarma. Elegí un número del 1 al 3: ")

                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    riesgo = input("Elegí un número del 1 al 3: ")

                if riesgo == "3":
                    alarma = True
                    print("¡Se activó la alarma!")
                else:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta!")

            else:

                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")


    elif opcion == "2":

        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando panel...")

        for paso in range(1, 5):

            codigo_parcial += "A"

            print(
                "Paso",
                paso,
                "- Código parcial:",
                codigo_parcial
            )

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1
            print("¡El hackeo abrió una cerradura!")


    elif opcion == "3":

        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10
            print("La alarma está activa: perdés 10 puntos extra de energía.")

        print("Descansaste.")


    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:

        bloqueado = True


print("\n=== FIN DEL JUEGO ===")

if cerraduras_abiertas == 3:

    print("¡VICTORIA!")
    print(nombre, "abrió la bóveda.")

elif bloqueado == True:

    print("DERROTA.")
    print("La alarma bloqueó el sistema.")

elif energia <= 0:

    print("DERROTA.")
    print("Te quedaste sin energía.")

elif tiempo <= 0:

    print("DERROTA.")
    print("Te quedaste sin tiempo.")
    