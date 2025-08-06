

usuario = {}
caractere_especial = '@#$%&*!'

#any()
#isdigit()
#len()
#isupper()

senha = 'senha@'
tem_maiuscula = any(c.isdigit() for c in senha)
tem_especial = any(c in caractere_especial for c in senha)
print(tem_especial)