import random
import string

def gerar_senha(tamanho=12):
    # Definir os caracteres possíveis para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Gerarando uma senha de 12 caracteres
senha = gerar_senha()
print("Senha gerada:", senha)
