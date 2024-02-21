from src.problema.problema import ProblemaMissionariosCanibais
from src.busca.busca import Solucao


def imprimir_solucao(solucao):
    if solucao:
        contador = 0
        for estado in solucao:
            print('Movimento', contador)
            print('Missionários:', estado.missionarios)
            print('Canibais:', estado.canibais)
            print('Barco:', estado.barco)
            print('------------')
            contador += 1
    else:
        print("Não foi encontrada uma solução para o problema.")


if __name__ == "__main__":
    problema = ProblemaMissionariosCanibais()
    busca = Solucao(problema)
    caminho_solucao = busca.buscar_solucao()
    imprimir_solucao(caminho_solucao)
