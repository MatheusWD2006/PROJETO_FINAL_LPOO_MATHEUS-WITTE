import sys

import os

sys.path.append(os.path.dirname(__file__))

from model.CulturaAnoTodo import CulturaAnoTodo
from model.CulturaEstacao import CulturaEstacao
from model.CulturaFactory import CulturaFactory
from model.estacao_enum import NomeEstacao

if __name__ == "__main__":
    cultura_ano_todo = CulturaFactory.criar_cultura(
        tipo_cultura="ANO_TODO",
        planta="Tomate",
        status=None
    )
    print(cultura_ano_todo.exibir_dados())
    print()

    cultura_estacao = CulturaFactory.criar_cultura(
        tipo_cultura="ESTACAO",
        planta="Alface",
        estacao=NomeEstacao.PRIMAVERA,
        status=None
    
    )
    print(cultura_estacao.exibir_dados())

    print()

    cultura_estacao.plantar()
    print(cultura_estacao.exibir_dados())

    print()

    cultura_estacao.colher()
    print(cultura_estacao.exibir_dados())

    print()

    cultura_ano_todo.plantar()
    print(cultura_ano_todo.exibir_dados())

    print()

    cultura_ano_todo.colher()
    print(cultura_ano_todo.exibir_dados())