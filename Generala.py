
import random
## 1 Tirada de dados: El programa simula la tirada de cinco dados y muestra los resultados.
def tirada ():
    seguir=False
    limite=3
    dados=[random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    while limite>0 and not seguir:
        limite-=1
        print(dados)
        rta=input("¿Desea volver a tirar? (si/no) ")
        if rta=="no":
            seguir=True
        else:
            posiciones=[]
            while len(posiciones)<5:
                pos=int(input("Ingrese el dado que desea volver a tirar (1-5) "))
                if pos>=1 and pos<=5 and pos not in posiciones:
                    posiciones.append(pos)
                else: 
                    print("Posición inválida o ya seleccionada. Intente nuevamente.")
            for pos in posiciones:
                dados[pos-1]=random.randint(1,6)
    return dados


def jugador1 ():
    partida1=[]
    resultado=tirada()
    partida1.append(resultado)
    print("Jugador 1:")
    print("Resultado final del Jugador 1:", resultado)
    return resultado
 
 for i in range de 