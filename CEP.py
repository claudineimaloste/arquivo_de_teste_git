import requests

def buscar_cep (cep):
    cep = cep.strip().replace('.','').replace(' ','').replace('-','')
    if len(cep) != 8 or not cep.isdigit():
        return 'Cep inválido'
        
    else:
    
        link = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(link)
        
        if resposta.status_code != 200:
            return 'Cep Não encontrado'
        else:
            cep_encontrado = resposta.json()
            return cep_encontrado

cep_digitado = input("Informe seu CEP: ")
resultado = buscar_cep(cep_digitado)

print(f"Logradouro: {resultado['logradouro']}")
print(f"Bairro: {resultado['bairro']}")
print(f"Cidade: {resultado['localidade']} - {resultado['uf']}")
