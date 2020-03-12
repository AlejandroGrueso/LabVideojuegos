import random
def main():
    cantimplora = 4
    cansancio = 0
    millas = 20
    sed = 0
    millas_enemy = 0
    print("Bienvenido a CAMELLO")
    print("Has robado un camello para cruzar el desierto de Gobi.")
    print("Los nativos quieren su camello de vuelta y te están persiguiendo.")
    print("Sobrevive al desierto y deshazte de los nativos")
    print(" ")
    done = False

    while (done is False):

        print("A.Beber de la cantimplora")
        print("B.Avanzar lento")
        print("C.Avanzar rápido")
        print("D.Descansar")
        print("E.Estado")
        print("Q.Salir")
        print("")
        x = str(input("¿Qué decides hacer?  "))
        choice = x.lower()
        if choice == ("q" or "Q"):
            salida = "Saliendo del juego..."
            print(salida.upper())
            done = True

        elif choice == ("a" or "A"):
            sed = 0
            cantimplora-=1
            print("Ya no tienes sed")
            print("Te quedan",cantimplora,"bebidas")
            print("")

        elif choice == ("b"):
            millas_enemy+=random.randint(6,15)
            millas+=random.randint(4,13)
            sed+=1
            cansancio+=1
            print("Has avanzado", millas,"millas")
            print("Los nativos han avanzado ", millas_enemy, "millas")
            print("")

        elif choice == ("c"):
            millas+=random.randint(10,20)
            millas_enemy+=random.randint(7,14)
            sed+=1
            cansancio+=random.randint(1,3)

        elif choice == ("d"):
            cansancio = 0
            millas_enemy+=random.randint(6,15)
            print("Tu camello esta feliz")
            print("Los nativos se acercan, distancia",millas_enemy,"millas")
            print("")


        elif choice == ("e" or "E"):
            print("Millas viajadas:", millas)
            print("Bebidas restantes:", cantimplora)
            print("Los nativos se encuantran a", millas_enemy, "millas")
            print("")


        if (millas > 200 or millas == 200):
            done = True
            ganar = "¡¡Has ganado!!"
            print(ganar.upper())

        if (millas_enemy > millas or millas_enemy == millas):
            done = True
            print("Te alcanzaron los nativos y recuperaron su camello")

main()