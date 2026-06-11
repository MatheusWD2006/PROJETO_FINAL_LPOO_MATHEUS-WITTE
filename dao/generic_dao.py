import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from abc import ABC, abstractmethod

class GenericDAO(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def remover(self, id_objeto):
        pass

    @abstractmethod
    def atualizar(self, objeto):
        pass