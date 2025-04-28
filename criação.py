# criar um arquivo

with open('arq1.txt', 'w') as arquivo:
    arquivo.write('Este é um novo arquivo de texto.')

# lê o arquivo 
arquivo = open('arq1.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()