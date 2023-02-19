

#23. Elabore um programa que leia o ano de nascimento de uma pessoa, leia o ano atual, e por
#fim, informe se ela já pode ou não tirar carteira de motorista. Lembrando que no Brasil a
#idade mínima para tirar CNH é 18 anos.


AnoN = int(input("Digite o Ano que Voce nasceu: "))

if (AnoN <= 2004):
    print(f"\nNascido em {AnoN}, Pode Tirar Habilitação!\n")
else:
    print(f"\nNascido em {AnoN}, Não Pode Tirar Habilitação!\n")