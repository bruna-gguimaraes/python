import os
# Caminho do arquivo
arquivo_caminho = r'c:/Users/bruna/Desktop/Faculdade/Lógica de Programação e Algoritmos - LPA/Python/'

# Verifica se o arquivo existe
if os.path.exists(arquivo_caminho):
    print(f"O arquivo {arquivo_caminho} foi encontrado.")
else:
    print(f"O arquivo {arquivo_caminho} não foi encontrado no diretório: {os.getcwd()}")
