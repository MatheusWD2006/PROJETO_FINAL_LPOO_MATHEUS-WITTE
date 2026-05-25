from model.cultura_estacao import CulturaEstacao
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura
from testes.teste_estacao import verao, outono, inverno, primavera
from model.estacao import Estacao
from testes.testeFactory import c1, c2
from model.StatusCulturaEstacao import StatusCulturaEstacao
from testes.teste_CulturaEstacao import milho 


milho_status = StatusCulturaEstacao(
    cultura_estacao=milho,
    data_plantio="15-09-2025",
    status="PLANTADO"
)

melancia_status = StatusCulturaEstacao(
    cultura_estacao=c1)

Uva= CulturaEstacao(
    nome="Uva",
    nome_cientifico="Vitis vinifera",
    descricao="Fruta cultivada principalmente em clima quente e seco.",
    tipo=TipoCultura.FRUTA,
    classificacao=ClassificacaoCultura.ANGIOSPERMA,
    estacao=verao,
    nota_produtividade=9,
    nota_resistencia=8
)

print(milho_status.exibir_dados())
milho.concluir()
milho_status.concluir()
print()
print(milho_status.exibir_dados())
print()
milho_status.concluir()
print(milho_status.exibir_dados())

print()
print(melancia_status.exibir_dados())

print()
print(Uva.exibir_dados())
