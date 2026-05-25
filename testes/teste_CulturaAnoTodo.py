from model.CulturaAnoTodo import CulturaAnoTodo
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura



cultura = CulturaAnoTodo(
    nome="Alface",
    nome_cientifico="Lactuca sativa",
    descricao="Cultura de plantio contínuo.",
    tipo=TipoCultura.VERDURA,
    classificacao=ClassificacaoCultura.ANGIOSPERMA,
)


print(cultura.exibir_dados())
print()
cultura.concluir()

print(cultura.exibir_dados())
