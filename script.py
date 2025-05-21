class pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Endereço:", self.endereco)

def validar():
    print("validando...")  # print em produção
    return True

def validar():  # função duplicada
    print("outra validação")
    return False

class Servico:
    def processar(self, dados):
        resultado = []
        for item in dados:
            resultado.append(item.lower().strip())
        for i in range(len(resultado)):
            for j in range(i + 1, len(resultado)):
                if resultado[i] == resultado[j]:
                    print("Duplicado:", resultado[i])  # print em produção
        return resultado

# Uso incorreto: método estático que não é marcado com @staticmethod
class Calculadora:
    def somar(a, b):
        return a + b

    def dividir(self, a, b):
        return a / b

calc = Calculadora()
print(calc.somar(10, 20))  # Erro de uso do método

p1 = pessoa("João", 30, "Rua A")
p1.dados()
