from src.models.categoria import Categoria as c

class Produtos():

    def __init__(self, categoria: c.Categoria, codProduto: str = '', descricao: str = ''):
        
        self.categoria = categoria 
        self.codProduto = codProduto
        self.descricao = descricao

    def get_produtos(self):
        '''Metodo que busca os produtos cadastrados'''


    def insert_produto(self):
        '''Metodo que insere novos produtos'''

    def atualizar_produtos(self):
        
        '''Metodo que atualiza o Produto'''