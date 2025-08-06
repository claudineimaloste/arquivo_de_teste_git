# Loop for

"""
Loop for
"""
"""
Loop é algo que se repete diversas vezes.
Em programação utilizamos eles para repetir uma tarefa várias vezes.

O for (Para) é uma das ferramentas que realizam esse loop.
Como declarar for em Python?
for item in sequencia:
    #Processo
Para cada item dentro de uma sequencia faça:
    #Processo
    
A sequencia deve ser iterável, mas o que é isso?
- São um conjunto de dados que podem ser desmembrados.
Exemplos de dados iteráveis:
a) Strings (Podem ser desmembradas por cada caracter)
"Filmes" -> 'F','i','l',...
Relembrando: Podemos pegar caracteres pelos indices da string.
Ex:
nome = 'Samantha'
print(nome[6]) # Irá imprimir o h
Curiosidade:
S a m a n t h a
0 1 2 3 4 5 6 7
      ...-3 -2 -1
nome = 'Samantha'
print(nome[2:-2]) # Irá imprimir o h
# Obs: Não é possível imprimir nome[-2:1], o python não fará a leitura quando o primeiro valor
# estiver casas a frente do último valor
print(nome[-2:1]) # Não irá imprimir

b) Listas,tuplas,dicionários e sets(conjuntos):
Ex:
Como declarar Listas?
nome = [1,2.5,True,'sim']
Logo, 
nome -> 1,2.5,True,'sim'
c) Função range():
O que ela faz?
 - Função que cria um intervalo de numeros escolhido pelo usuario.
Como declarar?
range(numero que você deseja que comece,numero que voce deseja que finalize + 1)
Ex:
numero = range(2,10) #Cria um intervalo de 2 a 9

Aplicações:
#Aplicação com string
seriado = 'Todo mundo odeia o Chris'
for letra in seriado: #Para cada letra dentro de seriado faça:
    print(letra, end='') #Por padrão o print imprime um por linha, usando end='' imprimimos na mesma linha
#Aplicação com Lista
numeros = [1,2,'oi',True]
for elemento in numeros: #Para cada elemento dentro de numeros faça:
    print(elemento)
#Aplicação com Range()
intervalo_num = range(3,11) #Valores de 3 a 10
for shrek in intervalo_num:
    print(shrek)
Complemento:
O range() pode ser utilizado por diversas formas:
a) range(2,10) #Cria uma sequencia de 2 a 9
b) range(10) #Cria uma sequencia de 0 a 9
c) range(-4,5) #Cria uma sequencia de -4 a 4
d) range(3,19,3) #Cria uma sequencia de 3 a 18 ao passo 3
e) range(18,4,-3) #Cria uma sequencia de 18 a 3 ao passo 3 negativo

# É possível utilizar condicionais dentro do loop:
#Achando numeros pares dentro de uma sequencia
for numero in range(2,20):
    if numero % 2 == 0: # Se o resto da divisão de numero por 2 for zero faça:
        print(f'Achei um numero par, numero:{numero}')
#Exemplo mais complexo, é possível ter for's consecutivos:
fruta ="abacate"
valor = range(1,4)
for letra in fruta:
    if letra == 'a':
        for num in valor:
            print('Achei a letra a')
Para sair antes que todo o loop seja executado, podemos utilizar a palavra break(Pausa).
Ex:
string = 'abcdefghijkl'

for letra in string:
    print(letra,end='/')
    if letra == 'g':
        break
Para prosseguir o loop utilizamos a palavra continue(prosseguir).
Ex:
string = 'abcdefghijkl'

for letra in string:
    if letra == 'g':
        continue
    print(letra,end='/')

Por fim, método enumerate():
O que faz?
- Basicamente adiciona um contador para cada elemento que foi desmembrado na sequencia.
Para declarar faça:
enumerate(variável)
# Ex:
heroi = 'Batman'
#Ao usar o enumerate
(0,'B'),(1,'a'),(2,'t'),...
for valor in enumerate(heroi):
    print(valor)
for contador,letra in enumerate(heroi):
    print(f'A {contador+1} letra e:{letra}')
for valor in enumerate(range(3,7)):
    print(valor)
for contador,letra in enumerate(range(3,7)):
    print(f'O {contador+1} numero e:{letra}')
"""
