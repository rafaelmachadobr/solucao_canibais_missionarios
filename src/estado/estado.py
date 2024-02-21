class Estado:
    """
    Classe que representa o estado do problema dos missionários e canibais.
    """

    def __init__(self, missionarios, canibais, barco):
        self.missionarios = missionarios
        self.canibais = canibais
        self.barco = barco

    def __eq__(self, other):
        return (
            self.missionarios == other.missionarios and
            self.canibais == other.canibais and
            self.barco == other.barco
        )

    def __hash__(self):
        return hash((self.missionarios, self.canibais, self.barco))
