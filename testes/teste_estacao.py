from datetime import date, datetime
from model.estacao import Estacao
from model.estacao_enum import NomeEstacao

verao = Estacao(
    nome=NomeEstacao.VERAO,
    temperatura_media=27.5,
    data_inicio="21-12-2025",  
    data_fim="20-03-2026",
    descricao="Estação quente com dias longos."
)
outono = Estacao(
    nome=NomeEstacao.OUTONO,
    temperatura_media=18,
    data_inicio="21-03-2025",
    data_fim="20-06-2025",
    descricao="Queda de folhas e transição para clima frio."
)

inverno = Estacao(
    nome=NomeEstacao.INVERNO,
    temperatura_media=9.5,
    data_inicio="21-06-2025",
    data_fim="22-09-2025",
    descricao="Frio, com geadas, chuva congelada e até neve ."
)

primavera = Estacao(
    nome=NomeEstacao.PRIMAVERA,
    temperatura_media=20.5,
    data_inicio="23-09-2025",
    data_fim="20-12-2025",
    descricao="Estação rica em flores e frutas."
)

if __name__ == "__main__":
 print(verao.exibir_dados())
 print()
 
 print(outono.exibir_dados())
 print()

 print(inverno.exibir_dados())
 print()

 print(primavera.exibir_dados())
 print()