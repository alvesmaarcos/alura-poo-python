class Carro:
    modelo = ''
    cor = ''
    ano = int

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'

carro = Carro(modelo='Tiggo 7 Sport', cor='Branco', ano=2025)

print(carro)

