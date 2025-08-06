# alunos = [{'nome':'Jonas','idade':15,'cpf':'12345678912'},
#           {'nome':'Marina','idade':15,'cpf':'98765432111'}
#           ]
alunos = {'100456':{'nome':'Jonas','idade':15,'cpf':'12345678912'},
          '100457':{'nome':'Marina','idade':15,'cpf':'98765432111'}
}


cpf = input('informe o matricula: ')
dados = alunos.get(cpf)

print(f'Nome: {dados['nome']}')
print(f'Idade: {dados['idade']}')
print(f'CPF: {dados['cpf']}')

# nome =input('informe o nome: ')
# idade = int(input('Informe a idade: '))
# cpf = input('Informe o CPF: ')

# novo_aluno = {'nome':nome,'idade':idade,'cpf':cpf}
# alunos.append(novo_aluno)
# print(alunos)

#  for i,nome in enumerate (alunos): 
    
#     print(f'Nome: {nome['nome']}\nIdade: {nome['idade']}\nCPF: {nome['cpf']}')



"""
Inserir um novo valor....
alunos = {'100':{'nome':'Afonso','idade':15},
          '101':{'nome':'Andre','idade': 15}}

nova_matricula = input('Informe a matricula')

nome = input('Nome: ')
idade = input('Idade: ')

alunos[nova_matricula] = {'nome':nome,'idade':idade}
 
# print(alunos)

for mat,dados in alunos.items():
    print(f'Matricula: {mat} | Nome: {dados['nome']} | Idade: {dados['idade']}')
"""
