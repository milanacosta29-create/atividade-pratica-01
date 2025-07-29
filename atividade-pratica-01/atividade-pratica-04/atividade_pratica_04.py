
# 1 - Calculadora simples
print("Calculadora")
num1 = float(input("Digite o primeiro n�mero: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo n�mero: "))

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("N�o � poss�vel dividir por zero.")
else:
    print("Operador inv�lido.")
# 2 - M�dia da turma
print("\nM�dia da turma")
quantidade = int(input("Quantos alunos? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / quantidade
print("M�dia da turma:", media)
# 3 - Verificador de senha
print("\nVerificador de senha")
senha = input("Digite uma senha: ")

tem_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and tem_numero:
    print("Senha forte.")
else:
    print("Senha fraca. Deve ter pelo menos 8 caracteres e 1 n�mero.")
# 4 - Classificador de n�meros
print("\nClassificador de n�meros (Par ou �mpar)")
pares = 0
impares = 0

while True:
    entrada = input("Digite um n�mero (ou 'sair' para terminar): ")
    if entrada.lower() == 'sair':
        break
    numero = int(entrada)
    if numero % 2 == 0:
        pares += 1
        print("Par")
    else:
        impares += 1
        print("�mpar")

print("Quantidade de pares:", pares)
print("Quantidade de �mpares:", impares)
