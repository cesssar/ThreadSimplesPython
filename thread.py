import threading
from time import sleep

class Teste():

    def __init__(self) -> None:
        pass

    def calcular_dobro(self, numero):
        print(f'O dobro de {numero} é {numero * 2}')


if __name__ == '__main__':
    robo = Teste()
    threads = []

    #cria as threads e os coloca numa lista sem executar elas
    for i in range(100):
        threads.append(threading.Thread(target=robo.calcular_dobro, args=(i,)))

    #executa as threads e quando chegar em determinado numero de execuções
    #dá um tempo de x segundos antes de dar start nas demais threads
    contador = 0
    for th in threads:
        th.start()
        contador += 1
        if contador == 10:
            sleep(2)
            contador = 0
