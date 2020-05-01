from Banco_Dados.Conexao import Conexao


class CriacaoTabela:

    @staticmethod
    def criar_tabela():
        try:
            connection = Conexao()
            sql = "CREATE TABLE REGISTROS_FOTOS(" \
                  "ID_USUARIO INTEGER PRIMARY KEY AUTOINCREMENT," \
                  "NOME VARCHAR(100) NOT NULL );"
            connection.cursor.execute(sql)
            print("_"*80)
            print("A Tabela foi criada com Sucesso(Nome Da Tabela: REGISTROS_FOTOS).")

        except():
            print("_"*80)
            print("Erro ao tentar criar a tabela.")
        finally:
            connection.fechar_conexao()

    @staticmethod
    def deletar_tabela():
        try:
            connection = Conexao()
            sql = "DROP TABLE REGISTROS_FOTOS;"
            connection.cursor.execute(sql)
            print("_"*80)
            print("A Tabela foi excluída com Sucesso.")

        except():
            print("_"*80)
            print("Erro ao tentar criar a tabela.")
        finally:
            connection.fechar_conexao()


# criar_tabela = CriacaoTabela()
# criar_tabela.deletar_tabela()
# criar_tabela.criar_tabela()


class OperacoesCrud:

    @staticmethod
    def gerar_id_usuario():
        try:
            connection = Conexao()
            sql = "SELECT COUNT(*) + 1 FROM REGISTROS_FOTOS;"
            connection.cursor.execute(sql)
            new_id = connection.cursor.fetchone()
            if new_id is not None:
                return new_id[0]
            else:
                return None

        except():
            print("_" * 80)
            print("Erro em geral ao tentar gerar o ID do Usuário")
            connection.fechar_conexao()

    @staticmethod
    def retornar_nome(id_usuario):
        try:
            connection = Conexao()
            sql = "SELECT NOME FROM REGISTROS_FOTOS WHERE ID_USUARIO = {0}; ".format(id_usuario)
            connection.cursor.execute(sql)
            nome_retornada = connection.cursor.fetchone()
            if nome_retornada is not None:
                return nome_retornada[0]
            else:
                return None

        except():
            print("_"*80)
            print("Erro em geral ao tentar retornar o nome do Usuário")
            connection.fechar_conexao()

    @staticmethod
    def inserir(id_usuario, nome):
        try:
            connection = Conexao()
            sql = "INSERT INTO REGISTROS_FOTOS VALUES({0}, '{1}');".format(id_usuario, nome.title())
            connection.cursor.execute(sql)
            connection.conexao.commit()
            print("_"*80)
            print(f"O Registro do Usuário({nome.title()}) foi criado no Banco de Dados.")

        except():
            print("_"*80)
            print("Erro em geral ao tentar realizar o Insert na tabela REGISTROS_FOTOS. ")
        finally:
            connection.fechar_conexao()

    @staticmethod
    def delete(id_usuario):
        try:
            connection = Conexao()
            sql = "DELETE FROM REGISTROS_FOTOS WHERE ID_USUARIO = {0};".format(id_usuario)
            connection.cursor.execute(sql)
            connection.conexao.commit()
            print("_"*80)
            print("O Registro foi excluíndo com suceso.")
        except():
            print("_"*80)
            print("Erro ao tentar excluir o registro.")
        finally:
            connection.fechar_conexao()


# insert = OperacoesCrud()
# print(insert.gerar_id_usuario())
# insert.inserir(insert.gerar_id_usuario(), "Ricardo")
# print(insert.retornar_nome(1))
# insert.delete(1)
