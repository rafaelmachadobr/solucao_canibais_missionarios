class Busca:
    """
    Classe base abstrata para implementar algoritmos de busca.
    """

    def __init__(self, problema):
        self.problema = problema

    def buscar_solucao(self):
        raise NotImplementedError(
            "Subclasses devem implementar o método buscar_solucao()")


class Solucao(Busca):
    """
    Classe para implementar a solução.
    """

    def buscar_solucao(self):
        fronteira = [[self.problema.estado_inicial]]
        explorado = []

        while fronteira:
            caminho = fronteira[0]
            fronteira = fronteira[1:]
            estado_final_caminho = caminho[-1]

            if estado_final_caminho in explorado:
                continue

            for movimento in self.problema.movimentos_possiveis(estado_final_caminho):
                if movimento in explorado:
                    continue
                fronteira.append(caminho + [movimento])

            explorado.append(estado_final_caminho)
            if estado_final_caminho == self.problema.estado_final:
                return caminho

        return None
