# 1 - Função que calcula a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# 2 - Função que verifica se é palíndromo
def verificar_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())  # remove espaços e pontuação
    return "Sim" if texto == texto[::-1] else "Não"

# 3 - Programa que calcula o preço final com desconto
def calcular_desconto():
    try:
        preco = float(input("Digite o preço original do produto: R$ "))
        desconto = float(input("Digite a porcentagem de desconto (%): "))
        valor_desconto = preco * (desconto / 100)
        preco_final = preco - valor_desconto
        print(f"Desconto: R$ {valor_desconto:.2f}")
        print(f"Preço final com desconto: R$ {preco_final:.2f}")
    except ValueError:
        print("Por favor, digite números válidos.")

# 4 - Programa que calcula quantos dias a pessoa está viva
from datetime import datetime

def dias_vivo():
    try:
        nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        hoje = datetime.now()
        dias_vividos = (hoje - data_nascimento).days
        print(f"Você está vivo há {dias_vividos} dias.")
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")

# Testes opcionais (descomente para usar individualmente)
# print(calcular_gorjeta(200, 10))  # Exemplo: gorjeta de R$ 20.0
# print(verificar_palindromo("Ame a ema"))  # Exemplo: Sim
# calcular_desconto()
# dias_vivo()
