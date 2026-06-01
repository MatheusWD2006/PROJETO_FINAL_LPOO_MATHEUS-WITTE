from dao.db_config import DBConfig

def conectar():
    conexao = DBConfig.get_connection()
    if conexao is not None:
        print("Conexão estabelecida com sucesso!")
    else:
        print("Falha ao estabelecer conexão.")
    return conexao