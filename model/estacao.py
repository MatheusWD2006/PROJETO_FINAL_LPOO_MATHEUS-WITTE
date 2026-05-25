from datetime import datetime, date
from model.estacao_enum import NomeEstacao


class Estacao:
    def __init__(self, nome, temperatura_media, data_inicio, data_fim, descricao, aviso_strategy=None):

        from model.estacao_strategy import selecionar_strategy, Avisos

        self.nome = nome
        self.temperatura_media = temperatura_media
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao

        if aviso_strategy is None:
            self.__aviso = selecionar_strategy(self)
        else:
            if not isinstance(aviso_strategy, Avisos):
                raise TypeError("aviso_strategy deve ser um objeto Avisos válido.")
            self.__aviso = aviso_strategy

   

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, NomeEstacao):
            raise TypeError("O campo 'nome' deve receber um valor do enum NomeEstacao.")
        self.__nome = valor

    @property
    def temperatura_media(self):
        return self.__temperatura_media

    @temperatura_media.setter
    def temperatura_media(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("temperatura_media deve ser número.")
        self.__temperatura_media = valor

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):

        if valor is None:
            raise ValueError("data_inicio não pode ser None. Informe uma data válida.")

        if isinstance(valor, date):
            self.__data_inicio = valor
            return

        if isinstance(valor, str):
            valor_limpo = valor.strip()
            try:
                self.__data_inicio = datetime.strptime(valor_limpo, "%d-%m-%Y").date()
            except ValueError:
                raise ValueError("data_inicio deve estar no formato dd-mm-YYYY.")

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, valor):

        if valor is None:
            raise ValueError("data_fim não pode ser None. Informe uma data válida.")

        if isinstance(valor, date):
            self.__data_fim = valor
            return

        if isinstance(valor, str):
            valor_limpo = valor.strip()
            try:
                self.__data_fim = datetime.strptime(valor_limpo, "%d-%m-%Y").date()
            except ValueError:
                raise ValueError("data_fim deve estar no formato dd-mm-YYYY.")
            

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def aviso(self):
        return self.__aviso

   

    def exibir_dados(self):
        aviso = self.__aviso.obter_aviso(self)
        return (
            f"Estação: {self.__nome.value}\n"
            f"Temperatura Média: {self.__temperatura_media}°C\n"
            f"Início: {self.__data_inicio}\n"
            f"Fim: {self.__data_fim}\n"
            f"Descrição: {self.__descricao}\n"
            f"Aviso da Estação: {aviso}"
        )

    def __str__(self):

        aviso = self.__aviso.obter_aviso(self)
        return (
            f"Estação: {self.__nome.value}\n"
            f"Temperatura Média: {self.__temperatura_media}°C\n"
            f"Início: {self.__data_inicio}\n"
            f"Fim: {self.__data_fim}\n"
            f"Descrição: {self.__descricao}"
            f"Aviso da Estação: {aviso}"
        )
