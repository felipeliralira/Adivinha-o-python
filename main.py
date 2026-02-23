import random as rd
print("-------------------------------------")
print("\nBem vindo ao jogo de adivinhação!\n")
print("-------------------------------------")


n_secreto = rd.randrange(1, 101)
n_tentativas = 5
rodada = 1

for rodada in range(1, n_tentativas + 1):
    print(f"rodada {rodada}/{n_tentativas}")
    entrada = int(input("digite um valor aleatório entre 1 e 100: "))
    acerto = entrada == n_secreto
    chutemaior = entrada > n_secreto
    chutemenor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("O valor digitado não é permitido")
        continue

    print(f"Você digitou o número: {entrada}")

    if(acerto):
        print("Parabéns, você acertou")
        break
    else:
        if(chutemaior):
            print("o número secreto é menor que seu chute")
        if(chutemenor):
            print("o número secreto é maior que seu chute")

    rodada = rodada + 1
print("Fim de Jogo!")