import requests

cep = '83606230'

link = f'https://viacep.com.br/ws/{cep}/json/'

cep_encontrado = requests.get(link)

if cep_encontrado.status_code == 200:

    dir_cep = cep_encontrado.json()

    print(f"CEP: {dir_cep['cep']}\nRua: {dir_cep['logradouro']}\nBairro: {dir_cep['bairro']}")
else:
    print("Cep não encontrado")