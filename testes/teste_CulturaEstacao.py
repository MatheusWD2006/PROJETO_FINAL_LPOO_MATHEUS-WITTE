from model.cultura_estacao import CulturaEstacao
from model.estacao_enum import NomeEstacao
from model.estacao import Estacao
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura
from testes.teste_estacao import verao, inverno, outono, primavera;


milho = CulturaEstacao(
    nome="Milho",
    nome_cientifico="Zea mays",
    descricao="Cultura comum no verão.",
    tipo=TipoCultura.GRAO,
    classificacao=ClassificacaoCultura.ANGIOSPERMA,
    estacao=verao,
    nota_produtividade=7.5,
    nota_resistencia=8.0,
)

verao2= Estacao(
    nome=NomeEstacao.VERAO,
    temperatura_media=29.5,
    data_inicio="21-12-2025",  
    data_fim="20-03-2026",
    descricao="Estação quente com dias longos."
)
             
if __name__ == "__main__":
 print(milho.exibir_dados())    
 milho.concluir()

 print()

 print(milho.exibir_dados())   
 print()

 print(verao2.exibir_dados())


