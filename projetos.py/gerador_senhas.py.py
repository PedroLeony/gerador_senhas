import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Aleatórias ===")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        if tamanho < 4:
            print("Por segurança, escolha um tamanho maior que 3.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Sua senha gerada é: {senha}")
    except ValueError:
        print("Por favor, digite um número válido.")

main()
