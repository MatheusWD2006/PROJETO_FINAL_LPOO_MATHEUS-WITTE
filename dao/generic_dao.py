import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from abc import ABC, abstractmethod

class GenericDAO(ABC):
    @abstractmethod
    # Salva o objeto no banco de dados.
    def salvar(self, objeto):
        pass

    @abstractmethod
    # Retorna todos os registros tratados por este DAO.
    def listar_todos(self):
        pass

    @abstractmethod
    # Remove o registro identificado no banco de dados.
    def remover(self, id_objeto):
        pass

    @abstractmethod
    # Atualiza o registro existente no banco de dados.
    def atualizar(self, objeto):
        pass