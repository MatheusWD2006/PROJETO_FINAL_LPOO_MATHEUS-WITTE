from abc import ABC, abstractmethod
from model.estacao_enum import NomeEstacao
from model.estacao import Estacao


class AvisoStrategy(ABC):
    @abstractmethod
    def gerar_aviso(self, estacao: "Estacao"):
        pass


class AvisoVerao(AvisoStrategy):
    def gerar_aviso(self, estacao: "Estacao"):
        return (
            "Cuidado com o calor e a exposição ao sol. "
            "Mantenha plantas bem irrigadas e protegidas do sol forte."
        )


class AvisoOutono(AvisoStrategy):
    def gerar_aviso(self, estacao: "Estacao"):
        return "Atenção às mudanças bruscas de temperatura e ventos fortes."


class AvisoInverno(AvisoStrategy):
    def gerar_aviso(self, estacao: "Estacao"):
        return "Cuidado com geadas e umidade alta. Evite irrigação excessiva."


class AvisoPrimavera(AvisoStrategy):
    def gerar_aviso(self, estacao: "Estacao"):
        return "Cuidado com temporais, ventos e alta umidade no ar."


class Avisos:
    def __init__(self, strategy: AvisoStrategy):
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, valor: AvisoStrategy):
        if not isinstance(valor, AvisoStrategy):
            raise TypeError("strategy deve ser uma instância de AvisoStrategy.")
        self.__strategy = valor

    def obter_aviso(self, estacao: "Estacao"):
        return self.__strategy.gerar_aviso(estacao)


def selecionar_strategy(estacao: "Estacao"):
    estacaoAviso = {
        NomeEstacao.VERAO: AvisoVerao(),
        NomeEstacao.OUTONO: AvisoOutono(),
        NomeEstacao.INVERNO: AvisoInverno(),
        NomeEstacao.PRIMAVERA: AvisoPrimavera()
    }
    return Avisos(estacaoAviso [estacao.nome])
