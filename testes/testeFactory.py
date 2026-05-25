from model.estacao_enum import NomeEstacao
from model.estacao import Estacao
from model.CulturaFactory import CulturaFactory
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura
from testes.teste_estacao import verao, outono, inverno, primavera



c1 = CulturaFactory.criar_cultura(
    "ESTACAO",
    nome="Melancia",
    nome_cientifico="Citrullus lanatus",
    descricao="Plantação de verão",
    tipo=TipoCultura.FRUTA,
    classificacao=ClassificacaoCultura.ANGIOSPERMA,
    estacao=verao,
    nota_produtividade=8,
    nota_resistencia=7
)


c2 = CulturaFactory.criar_cultura(
    "ANO_TODO",
    nome="Rúcula",
    nome_cientifico="Eruca sativa",
    descricao="Cultivo contínuo o ano todo",
    tipo=TipoCultura.VERDURA,
    classificacao=ClassificacaoCultura.ANGIOSPERMA
)
if __name__ == "__main__":
    print(c1.exibir_dados())
    c1.concluir()
    print()
    print(c1.exibir_dados())
    print()

    print(c2.exibir_dados())
    c2.concluir()
    print()
    print(c2.exibir_dados())