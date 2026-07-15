class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, ano_publicacao):
        self._ano_publicacao = ano_publicacao

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = bool(valor)

    def __str__(self):
        header = f"{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano de publicação'.ljust(25)}"
        info = f"{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano_publicacao).ljust(25)}"
        return header + '\n' + info
    
    @classmethod
    def emprestar(self):
        self.disponivel = False

    @classmethod
    def verificar_disponibilidade(cls):
        for livro in Livro.livros:
            if livro.disponivel and livro.ano_publicacao == 2026:
                print(livro.__str__())


# livro1 = Livro('Livro 1', 'Ana', 2026)
# livro2 = Livro('Livro 2', 'Bia', 2002)

# 
# print(livro1.__str__())
# print(livro2.__str__())
# 
# livro2.emprestar()
# print(livro2.disponivel)

# Livro.verificar_disponibilidade()