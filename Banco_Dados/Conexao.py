import sqlite3


class Conexao:
    def __init__(self):
        conexao = sqlite3.connect("BD_USUARIOS_REC_FACIAL")
        cursor = conexao.cursor()
        self.cursor = cursor
        self.conexao = conexao
        print("Conexão Aberta")

    def fechar_conexao(self):
        self.conexao.close()
        print("Conexao Fechada")
