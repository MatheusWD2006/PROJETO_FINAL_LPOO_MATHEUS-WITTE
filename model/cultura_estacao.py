from model.estacao_enum import NomeEstacao


class CulturaEstacao:

    def __init__(self, planta, estacao: NomeEstacao, nota_produtividade=0, nota_resistencia=0, recomendado="NÃO"):

        self.planta = planta

        if not isinstance(estacao, NomeEstacao):
            raise TypeError("estacao deve ser um objeto NomeEstacao.")
        self.__estacao = estacao

        self.nota_produtividade = nota_produtividade
        self.nota_resistencia = nota_resistencia

        self.__recomendado = recomendado


    @property
    def estacao(self):
        return self.__estacao

    @property
    def nota_produtividade(self):
        return self.__nota_produtividade

    @nota_produtividade.setter
    def nota_produtividade(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_produtividade deve ser número.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_produtividade deve estar entre 0 e 10.")
        self.__nota_produtividade = valor

    @property
    def nota_resistencia(self):
        return self.__nota_resistencia

    @nota_resistencia.setter
    def nota_resistencia(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_resistencia deve ser numérica.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_resistencia deve estar entre 0 e 10.")
        self.__nota_resistencia = valor

    @property
    def recomendado(self):
        return self.__recomendado


    def concluir(self):

        if self.__nota_produtividade >= 6 and self.__nota_resistencia >= 6:
            self.__recomendado = "SIM"

    def exibir_dados(self):
         return (
            f"{self.planta}\n"
            f"Estação: {self.__estacao.nome.value}\n"
            f"Nota Produtividade: {self.__nota_produtividade}\n"
            f"Nota Resistência: {self.__nota_resistencia}\n"
            f"Recomendado: {self.__recomendado}"
        )


    def __str__(self):
        return self.exibir_dados()
