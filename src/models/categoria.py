
class Categoria():
    def __init__(self, codCategoria = '', descricaoCategoria = ''):

        self.codCategoria = codCategoria
        self.descricaoCategoria = descricaoCategoria

    def get_categoria(self):
        '''Metodo que busca as categorias cadastradas'''

        consulta = """
            select 
                "codCategoria",
                "nomeCategoria"
            from 
                "Diogo"."categorias"
            """

    def inserir_categorias(self):
        '''Metodo que inseri novas categorias'''

    def alterar_categoria(self):
        '''Metodo que altera as categorias do sistema'''
        