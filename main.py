import os
from traceback import print_tb


class No:
    def __init__(self, valor, pai=None) -> None:
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
                no.esquerdo = No(valor, no)
                self.balancear_arvore(no.esquerdo)
        if valor > no.valor:
            if no.direito:
                self._inserir(valor, no.direito)
            else:
                no.direito = No(valor, no)
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
                self._remover(valor, no.esquerdo)
        elif valor > no.valor:
            if no.direito:
                self._remover(valor, no.direito)
        elif valor == no.valor:
            if not no.esquerdo and not no.direito:
                # Primeiro caso: Se o nó removido não tem nenhum filho
                noh_pai = no.pai
                if noh_pai:
                    if noh_pai.esquerdo == no:
                        noh_pai.esquerdo = None
                    if noh_pai.direito == no:
                        noh_pai.direito = None
                else:
                    self.root = None

                del no
                self.balancear_arvore(noh_pai)
            elif no.esquerdo and not no.direito:
                # Segundo caso: Se o nó removido tem apenas filho esquerdo
                noh_pai = no.pai
                # parent to child relationship
                if noh_pai:
                    if noh_pai.esquerdo == no:  # which we want to remove
                        noh_pai.esquerdo = no.esquerdo
                    elif noh_pai.direito == no:
                        noh_pai.direito = no.esquerdo
                else:
                    self.root = no.esquerdo
                # child to parent relationship
                no.esquerdo.pai = noh_pai
                del no
                self.balancear_arvore(noh_pai)
            elif no.direito and not no.esquerdo:
                # Terceiro caso: Se o nó removido tem apenas filho direito
                noh_pai = no.pai
               
                if noh_pai:
                    if noh_pai.esquerdo == no: 
                        noh_pai.esquerdo = no.direito
                    elif noh_pai.direito == no:
                        noh_pai.direito = no.direito
                else:
                    self.root = no.direito
                
                no.direito.pai = noh_pai
                del no
                self.balancear_arvore(noh_pai)
            elif no.direito and no.esquerdo:
                # Quarto caso: Se o nó removido tem os dois filhos
                noh_sucessor = self.retorna_sucessor(no.direito)
                # Trocar o valores
                noh_sucessor.valor, no.valor = no.valor, noh_sucessor.valor
                self._remover(noh_sucessor.valor, no.direito)
                
    def retorna_sucessor(self, no: No):
        if no.esquerdo:
            return self.retorna_sucessor(no.esquerdo)
        return no

    def balancear_arvore(self, no: No):
        # Vai andar até a raiz verificando se há algum nó desbalanceado
        while no: 
            no.altura = max(self.retorna_altura(no.esquerdo), self.retorna_altura(no.direito)) + 1
            self.arrumar_arvore(no)
            no = no.pai # Subindo até o nó raiz

    def arrumar_arvore(self, no: No):
        if self.retorna_desbalanceamento(no) > 1:
            if self.retorna_desbalanceamento(no.esquerdo) < 0:
                self.rotacioanar_esquerda(no.esquerdo)
            self.rotacionar_direita(no)
        if self.retorna_desbalanceamento(no) < -1:
            if self.retorna_desbalanceamento(no.direito) > 0:
                self.rotacionar_direita(no.direito)
            self.rotacioanar_esquerda(no)

    def rotacionar_direita(self, no: No):
        temp_noh_esquerdo = no.esquerdo
        temp_subnoh_direito = no.esquerdo.direito

        temp_noh_esquerdo.direito = no
        no.esquerdo = temp_subnoh_direito

        temp_pai = no.pai
        temp_noh_esquerdo.pai = temp_pai
        no.pai = temp_noh_esquerdo

        if temp_subnoh_direito:
            temp_subnoh_direito.pai = no
        
        if temp_noh_esquerdo.pai:
            if temp_noh_esquerdo.pai.esquerdo == no:
                temp_noh_esquerdo.pai.esquerdo = temp_noh_esquerdo
            elif temp_noh_esquerdo.pai.direito == no:
                temp_noh_esquerdo.pai.direito = temp_noh_esquerdo
        else:
            self.root = temp_noh_esquerdo

        no.altura = max(self.retorna_altura(no.esquerdo), self.retorna_altura(no.direito)) + 1
        temp_noh_esquerdo.altura = max(self.retorna_altura(temp_noh_esquerdo.esquerdo), self.retorna_altura(temp_noh_esquerdo.direito)) + 1
        
        print('\nRotacionando o valor', no.valor, 'para direta.')

    def rotacioanar_esquerda(self, no: No):
        temp_noh_direto = no.direito
        temp_subnoh_esquerdo = no.direito.esquerdo

        temp_noh_direto.esquerdo = no
        no.direito = temp_subnoh_esquerdo

        temp_noh_pai = no.pai
        temp_noh_direto.pai = temp_noh_pai
        no.pai = temp_noh_direto
    
        if temp_subnoh_esquerdo:
            temp_subnoh_esquerdo.pai = no

        if temp_noh_direto.pai: 
            if temp_noh_direto.pai.esquerdo == no:
                temp_noh_direto.pai.esquerdo = temp_noh_direto
            elif temp_noh_direto.pai.direito == no:
                temp_noh_direto.pai.direito = temp_noh_direto
        
        else:
            self.root = temp_noh_direto

        no.altura = max(self.retorna_altura(no.esquerdo), self.retorna_altura(no.direito)) + 1
        temp_noh_direto.altura = max(self.retorna_altura(temp_noh_direto.esquerdo), self.retorna_altura(temp_noh_direto.direito)) + 1

        print('\nRotacionando o valor', no.valor, 'para esquerda.')

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

        print(no.valor)

        if no.direito:
            self.percuso_emordem(no.direito)

    def busca(self, valor):
        if self.root:
            return self.buscar_valor(valor, self.root)

    def buscar_valor(self, valor, no: No):
        try:
            if valor < no.valor:
                if no.esquerdo:
                    return self.buscar_valor(valor, no.esquerdo)
            elif valor > no.valor:
                if no.direito:
                    return self.buscar_valor(valor, no.direito)
            elif valor == no.valor:
                return no
            return False
        except TypeError:
            return "Tipo inválido"

    def menu(self):
        while True:
            print("========== ARVORE - AVL ==========")
            print("1 - Inserir")
            print("2 - Remover")
            print("3 - Buscar")
            print("4 - Impressão dos valor no percusso em ordem")
            print("5 - Fechar programa")
            op = int(input("Opção: "))
            
            if op == 5 :
                print("Fechando programa...")
                break

            if op == 1:
                valor = int(input("Digite o valor para inserir: "))
                self.inserir(valor)
            elif op == 2:
                valor = int(input("Digite o valor para remover: "))
                self.remover(valor)
            elif op == 4:
                print("Valores no percuso em ordem")
                if self.root:
                    self.percuso_emordem(self.root)
                else:
                    print("Arvore vazia")
            elif op == 3:
                valor = int(input("Digite o valor para busca: "))
                valorDaBusca = self.busca(valor)
                if valorDaBusca:
                    print("Item encontrado: ", valorDaBusca.valor)
                else: 
                    print("Item não encontrado")

avl = ArvoreAvl()

avl.menu()
