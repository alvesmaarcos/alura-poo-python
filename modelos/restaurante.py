class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    criado = ''
    telefone = ''

    def __init__(self, nome, categoria, criado, telefone):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.criado = criado
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Criado: {self.criado}, Telefone: {self.telefone}.'

restaurante = Restaurante("Comida's", 'Nordestina', '10/07/2026', '(11) 9.9999-9999')

print(restaurante)