class Cliente:
    nome = ''
    altura_cm = int
    idade = int

    def __init__(self, nome, altura_cm, idade):
        self.nome = nome
        self.altura_cm = altura_cm
        self.idade = idade
        clientes.append(self)

    def __str__(self):
        return f'Nome: {self.nome}, Altura(cm): {self.altura_cm}, Idade: {self.idade}'
    
    

clientes = []

cliente1 = Cliente('Ana', 165, 18)
cliente2 = Cliente('João', 181, 19)
cliente3 = Cliente('Lucas', 171, 20)

def listar_clientes():
        for cliente in clientes:
            print(cliente)

listar_clientes()