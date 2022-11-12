#Heap de maximo é de minimo com as operações de inserção, remoção e troca de prioridade

class Heap:
    def __init__(self, tipo):
        self.heap = []
        self.tipo = tipo

    def pai(self, i):
        return (i - 1) // 2

    def esquerda(self, i):
        return 2 * i + 1

    def direita(self, i):
        return 2 * i + 2

    def troca(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def subir(self, i):
        if self.tipo == 'max':
            while i != 0 and self.heap[self.pai(i)] < self.heap[i]:
                self.troca(i, self.pai(i))
                i = self.pai(i)
        else:
            while i != 0 and self.heap[self.pai(i)] > self.heap[i]:
                self.troca(i, self.pai(i))
                i = self.pai(i)

    def descer(self, i):
        if self.tipo == 'max':
            while self.esquerda(i) < len(self.heap):
                maior = self.esquerda(i)
                if self.direita(i) < len(self.heap) and self.heap[self.direita(i)] > self.heap[maior]:
                    maior = self.direita(i)
                if self.heap[i] >= self.heap[maior]:
                    break
                self.troca(i, maior)
                i = maior
        else:
            while self.esquerda(i) < len(self.heap):
                menor = self.esquerda(i)
                if self.direita(i) < len(self.heap) and self.heap[self.direita(i)] < self.heap[menor]:
                    menor = self.direita(i)
                if self.heap[i] <= self.heap[menor]:
                    break
                self.troca(i, menor)
                i = menor

    def inserir(self, k):
        self.heap.append(k)
        self.subir(len(self.heap) - 1)

    def remover(self):
        if len(self.heap) == 0:
            return
        self.troca(0, len(self.heap) - 1)
        self.heap.pop()
        self.descer(0)

    def trocar(self, i, k):
        self.heap[i] = k
        self.subir(i)
        self.descer(i)

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, i):
        return self.heap[i]
    
    def __setitem__(self, i, k):
        self.heap[i] = k
    
    def __delitem__(self, i):
        del self.heap[i]

#Cria um menu para o usuario escolher qual operação deseja fazer
def menu():
    print ('0 - Criar heap e 0escolher o tipo')
    print('1 - Inserir')
    print('2 - Remover')
    print('3 - Trocar')
    print('4 - Imprimir')
    print('5 - Sair')
    return int(input('Escolha uma opção: '))
#Loop para o menu 
while True:
    op = menu()
    if op == 0:
        tipo = input('Digite max para criar um heap de maximo ou min para criar um heap de minimo: ')
        heap = Heap(tipo)
    elif op == 1:
        heap.inserir(int(input('Digite o valor a ser inserido: ')))
    elif op == 2:
        heap.remover()
    elif op == 3:
        i = int(input('Digite a posição do elemento a ser trocado: '))
        k = int(input('Digite o novo valor: '))
        heap.trocar(i, k)
    elif op == 4:
        print(heap)
    elif op == 5:
        break
    else:
        print('Opção inválida')
