import random
import string
import requests

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    dados = resposta.json()

    nome = dados['results'][0]['name']['first'] + ' ' + dados['results'][0]['name']['last']
    email = dados['results'][0]['email']
    pais = dados['results'][0]['location']['country']

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            print("Logradouro:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])
        else:
            print("CEP não encontrado.")
    else:
        print("Erro na requisição.")

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        if chave in dados:
            info = dados[chave]
            print("Moeda:", info["name"])
            print("Cotação atual: R$", info["bid"])
            print("Máximo do dia: R$", info["high"])
            print("Mínimo do dia: R$", info["low"])
            print("Última atualização:", info["create_date"])
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro na requisição.")

if __name__ == "__main__":
    escolha = input("Digite 'senha' para gerar senha, 'usuario' para gerar usuário, 'cep' para consultar CEP ou 'cotacao' para consultar cotação: ").strip().lower()
    if escolha == 'senha':
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
    elif escolha == 'usuario':
        gerar_usuario()
    elif escolha == 'cep':
        cep_usuario = input("Digite o CEP (somente números): ")
        consultar_cep(cep_usuario)
    elif escolha == 'cotacao':
        moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
        consultar_cotacao(moeda_usuario)
    else:
        print("Opção inválida.")