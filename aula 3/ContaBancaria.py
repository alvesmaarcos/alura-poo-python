class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativa = False

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R$ {self.saldo}'
    
    def ativar_conta(self):
        self.ativa = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativa(self):
        return self._ativa
    
    @titular.setter
    def titular(self, titular):
        if isinstance(titular, str):
            self._titular = titular
        else:
            print('Nome do titular precisa ser String.')
            return
        
    @saldo.setter
    def saldo(self, saldo):
        if isinstance(saldo, float):
            self._saldo = saldo
        else:
            print('Saldo precisa ser número.')
            return
        
    @ativa.setter
    def ativa(self, ativa):
        if isinstance(ativa, bool):
            self._ativa = ativa
        else:
            print('A conta pode apenas estar ativa (True) ou inativa (False).')
            return

conta1 = ContaBancaria('Ana', 10.00)
print(conta1.__str__())
conta2 = ContaBancaria('Bruno', 15.00)
print(conta2.__str__())
conta3 = ContaBancaria('Carlos', 20.00)
conta3.ativar_conta()
print(conta3.__str__(), conta3.ativa)

conta4 = ContaBancaria('Davi', 25.00)
print(conta4.titular)




#################################################################




class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self._nome = nome
        else:
            print('Nome precisa ser uma string válida.')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int) and idade >= 0:
            self._idade = idade
        else:
            print('Idade precisa ser um número inteiro não negativo.')

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, str) and endereco.strip():
            self._endereco = endereco
        else:
            print('Endereço precisa ser uma string válida.')

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str) and cpf.strip():
            self._cpf = cpf
        else:
            print('CPF precisa ser uma string válida.')

    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, profissao):
        if isinstance(profissao, str) and profissao.strip():
            self._profissao = profissao
        else:
            print('Profissão precisa ser uma string válida.')

    @classmethod
    def criar_conta(cls):
        conta = ContaBancaria(cls.nome, 0)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta5 = cliente1.criar_conta()
print(conta5.__str__())