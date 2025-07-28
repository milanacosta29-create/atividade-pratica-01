# --- Atividade 2: Calculadora de Desconto ---

# 1. Definir as informações do produto
nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20 # Representa 20%

# 2. Calcular o valor do desconto
# Convertemos a porcentagem para um número decimal (ex: 20% = 0.20)
valor_do_desconto = preco_original * (porcentagem_de_desconto / 100)

# 3. Calcular o preço final após o desconto
preco_final = preco_original - valor_do_desconto

# 4. Arredondar os valores para duas casas decimais (embora aqui não seja estritamente necessário, é bom praticar)
valor_do_desconto_arredondado = round(valor_do_desconto, 2)
preco_final_arredondado = round(preco_final, 2)

# 5. Exibir os detalhes
print("\n--- Calculadora de Desconto ---")
print(f"Nome do Produto: {nome_do_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_de_desconto}%")
print(f"Valor do Desconto: R$ {valor_do_desconto_arredondado:.2f}")
print(f"Preço Final: R$ {preco_final_arredondado:.2f}")