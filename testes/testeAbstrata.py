from model.cultura import Cultura
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura

print("Tentando instanciar Cultura (classe abstrata)...\n")

try:
    cultura = Cultura(
        nome="Teste",
        nome_cientifico="Testus exemplus",
        descricao="Tentativa de instanciar classe abstrata.",
        tipo=TipoCultura.GRAO,
        classificacao=ClassificacaoCultura.ANGIOSPERMA
    )

except TypeError as e:
    print("ERRO OCORRIDO AO CRIAR OBJETO:")
    print(e)
