# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se
#  ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

print("alistamento militar")
idade = int(input("insira sua idade:"))

if idade < 18 :
    print(f"você ainda não tem idade suficiente para se alistar faltam:{18 - idade} anos")
elif idade == 18 :   
    print(f"você está na idade certa para se alistar")
else :
    print(f"você está atrasado para o alistamento em { idade - 18} anos")    