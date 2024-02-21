from ..estado.estado import Estado


class ProblemaMissionariosCanibais:
    """
    Classe que representa o problema dos missionários e canibais,
    com as regras e lógica para solução.
    """

    def __init__(self):
        self.estado_inicial = Estado(3, 3, 1)
        self.estado_final = Estado(0, 0, 0)

    def movimentos_possiveis(self, estado):
        """
        Retorna uma lista de movimentos possíveis a partir do estado dado.
        """

        possibilidades = []
        miss, cani, barco = estado.missionarios, estado.canibais, estado.barco

        def add_possibilidade(miss2, cani2):
            if 0 <= miss2 <= 3 and 0 <= cani2 <= 3:
                possibilidades.append(Estado(miss2, cani2, 1 - barco))

        for i in range(3):
            for j in range(3):
                if 0 < i + j <= 2:
                    if barco == 1:
                        miss2, cani2 = miss - i, cani - j
                    else:
                        miss2, cani2 = miss + i, cani + j

                    add_possibilidade(miss2, cani2)

        return possibilidades
