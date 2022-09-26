class No:
    def __init__(self, valor, pai) -> None:
        self.valor = valor
        self.pai = pai
        self.height = 0

class ArvoreAvl:
    def __init__(self) -> None:
        self.root = None

    def inserir(self, valor): 
        if not self.root: # Se ainda não tiver um nó raiz, adiciona
            self.root = No(valor)
        else:
            self._inserir(valor, self.root)        

    def _inserir(self, valor, root):
        ...

    def remover(self, valor):
        if not self.root:
            print("Não há dado para ser removido")
        else:
            self._remover(valor, self.root)

    def _remover(self, valor, root):
        ...
    