try:
    with open('arq1.txt', 'x') as arquivo:
        arquivo.write('Este arquivo é criado exclusivamente.')
except FileExistsError:
    print('O arquivo já existe.') #ira dar erro, pois o arquivo já existe, FileExisrsError permite fazer essa verificação

arquivo = open('arq1.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

