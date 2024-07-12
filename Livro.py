class Livro:
    def __init__(self,nome:str,autor:str,editora:str,pags:int) -> None:
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = pags

    def getPaginas(self):
        print(self.paginas)

    def setEditora(self,nomenovo):
        self.editora = nomenovo



livro4.getPaginas()

print(livro4.editora)

livro4.setEditora(123)

print(livro4.editora)

print("BLABLABLA")
print("BLABLABLA")
print("BLABLABLA")
print("BLABLABLA")