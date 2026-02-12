print("-------------------------------------")
print("\nBem vindo ao jogo de adivinhação!\n")
print("-------------------------------------")

#Definição de variáveis
n_secreto = 68
entrada = int (input("digite um valor numérico: "))
acertou = entrada == n_secreto
entrada_maior = entrada > n_secreto
entrada_menor = entrada < n_secreto

print(f"Você digitou o número {entrada}")

#Verificação de acerto e erro
if(acertou):
    print("Parabéns, você acertou o número secreto")
else:
    if(entrada_maior):
        print("O número digitado foi maior do que o número secreto")
    if(entrada_menor):
        print("O número digitado foi menor do que o número secreto")


print("Fim de jogo!")
