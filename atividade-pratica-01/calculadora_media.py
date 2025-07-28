# --- Atividade 3: Calculadora de M�dia Escolar ---

# 1. Definir as notas
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# 2. Calcular a soma das notas
soma_das_notas = nota1 + nota2 + nota3

# 3. Calcular a m�dia (dividindo pela quantidade de notas)
quantidade_de_notas = 3
media = soma_das_notas / quantidade_de_notas

# 4. Arredondar a m�dia para duas casas decimais
media_arredondada = round(media, 2)

# 5. Exibir as notas e o resultado final
print("\n--- Calculadora de M�dia Escolar ---")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"M�dia Final: {media_arredondada:.2f}")