from model.cultura import Cultura
from model.estacao import Estacao


class CulturaEstacao(Cultura):

    def __init__(self, nome, nome_cientifico, descricao, tipo, classificacao,
                 estacao: Estacao,
                 nota_produtividade,
                 nota_resistencia, recomendado="NÃO"):

        super().__init__(nome, nome_cientifico, descricao, tipo, classificacao)

        if not isinstance(estacao, Estacao):
            raise TypeError("estacao deve ser um objeto Estacao.")
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
            f"{super().__str__()}\n"
            f"{self.__estacao.exibir_dados()}\n"
            f"Estação: {self.__estacao.nome.value}\n"
            f"Nota Produtividade: {self.__nota_produtividade}\n"
            f"Nota Resistência: {self.__nota_resistencia}\n"
            f"Recomendado: {self.__recomendado}"
        )


    def __str__(self):
        return self.exibir_dados()
