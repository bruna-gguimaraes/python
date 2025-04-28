# função open()

arquivo = open('manipulação.txt', 'w')
arquivo.write('teste 2')
arquivo.close()

# lê o arquivo 
arquivo = open('manipulação.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()




