#idade = input('Qual é a sua idade?')
#print(idade)


#outro exemplo usando fstring

#nome = input ('Qual é seu nome?')
#print(f' Olá {nome}, seja bem-vindo (a)')

# exercicio
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

#modelo moderno
soma = 'O resultado da soma de {} com {} é {}.'.format(x,y,x + y)
print(soma)

#maneira com f-string

soma = f'O resultado da soma de {x} com {y} é {x + y}.'
print(soma)