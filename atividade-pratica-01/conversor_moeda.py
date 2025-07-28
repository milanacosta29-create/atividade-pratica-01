# --- Atividade 1: Conversor de Moeda ---

# 1. Definir os dados fornecidos
valor_em_reais = 100.00
taxa_do_dolar = 5.20
taxa_do_euro = 6.15

# 2. Calcular a conversão para Dólar
valor_em_dolar = valor_em_reais / taxa_do_dolar

# 3. Calcular a conversão para Euro
valor_em_euro = valor_em_reais / taxa_do_euro

# 4. Arredondar os valores para duas casas decimais
valor_em_dolar_arredondado = round(valor_em_dolar, 2)
valor_em_euro_arredondado = round(valor_em_euro, 2)

# 5. Exibir os resultados
print("--- Conversor de Moeda ---")
print(f"Valor em Reais: R$ {valor_em_reais:.2f}") # .2f formata para 2 casas decimais
print(f"Taxa do Dólar: R$ {taxa_do_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_do_euro:.2f}")
print(f"Valor convertido para Dólar: US$ {valor_em_dolar_arredondado:.2f}")
print(f"Valor convertido para Euro: € {valor_em_euro_arredondado:.2f}")