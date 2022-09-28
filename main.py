class No:
    def __init__(self, valor, pai) -> None:
        self.valor = valor
        self.pai: No = pai
        self.esquerdo: No = None
        self.direito: No = None
        self.altura = 0

class ArvoreAvl:
    def __init__(self) -> None:
        self.root = None

    def inserir(self, valor): 
        if not self.root: # Se ainda não tiver um nó raiz, adiciona
            self.root = No(valor)
        else:
            self._inserir(valor, self.root)        

    def _inserir(self, valor, no: No):
        if valor < no.valor:
            if no.esquerdo:
                self._inserir(valor, no.esquerdo)
            else:
                no.esquerdo = No(valor, pai=no)
                self.balancear_arvore(no.esquerdo)
        if valor > no.valor:
            if no.direito:
                self._inserir(valor, no.direito)
            else:
                no.direito = No(valor, pai=no)
                self.balancear_arvore(no.direito)

    def remover(self, valor):
        if not self.root:
            print("Não há dado para ser removido")
        else:
            self._remover(valor, self.root)

    def _remover(self, valor, no: No):
        # Encontrando nó
        if valor < no.valor:
            if no.esquerdo:
                self._remover(valor, no)
        elif valor > no.valor:
            if no.direito:
                self._remover(valor, no.direito)
        elif valor == no.valor:
            if not no.esquerdo and not no.direito:
                # Primeiro caso: Se o nó removido não tem nenhum filho
                if no.pai:
                    if no.pai.esquerdo == no:
                        no.pai.esquerdo = None
                    if no.pai.direito == no:
                        no.pai.direito = None
                else:
                    self.root = None
            elif no.esquerdo and not no.direito:
                # Segundo caso: Se o nó removido tem apenas filho esquerdo
                pai = no.pai
                if pai:
                    if pai.esquerdo == no:
                        pai.esquerdo == no.esquerdo
                    if pai.direito == no:
                        pai.direito = no.direito
                else:
                    self.root = no.esquerdo

                no.esquerdo.pai = pai
                del no
                self.balancear_arvore(pai)
            elif no.direito and not no.esquerdo:
                # Terceiro caso: Se o nó removido tem apenas filho direito
                pai = no.pai
                if pai:
                    if pai.esquerdo == no:
                        pai.esquerdo == no.esquerdo
                    if pai.direito == no:
                        pai.direito = no.direito
                else:
                    self.root = no.direito

                no.direito.pai = pai
                del no
                self.balancear_arvore(pai)
            elif no.direito and no.esquerdo:
                # Quarto caso: Se o nó removido tem os dois filhos
                noh_sucesso = self.retorna_sucessor(no.direito)
                # Trocar o valores
                noh_sucesso.valor, no.valor = noh_sucesso.valor, no.valor
                self._remover(noh_sucesso.valor, no.direito)
                
    def retorna_sucessor(self, no: No):
        if no.esquerdo:
            return self.retorna_sucessor(no.esquerdo)
        return no

    def balancear_arvore(self, no: No):
        # Vai andar até a raiz verificando se há algum nó desbalanceado
        while no: 
            no.altura = max(self.retorna_altura(no.esquerdo) - self.retorna_altura(no.direito)) + 1

            if self.retorna_desbalanceamento(no) > 1:
                # Desbalanceamento do lado esquerdo
                if self.retorna_desbalanceamento(no.esquerdo) < 0:
                    # Gira para o esquerdo
                    ...
                # Gira para o direito
            if self.retorna_desbalanceamento(no) < -1:
                # Desbalanceamento do lado direito
                if self.retorna_desbalanceamento(no.direito) < 0:
                    ...
                    # Gira para o direito
                # Gira para o esquerdo

            no = no.pai # Subindo até o nó raiz

    

    def retorna_altura(self, no: No):
        if not no:
            return -1
        return no.altura

    def retorna_desbalanceamento(self, no: No):
        if not no:
            return 0
        return self.retorna_altura(no.esquerdo) - self.retorna_altura(no.direito)

    def percuso_emordem(self, no: No):
        if no.esquerdo:
            self.percuso_emordem(no.esquerdo)

        print(no.data)

        if no.direito:
            self.percuso_emordem(no.direito)