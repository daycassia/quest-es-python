#Salario: Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
n_f=int(input())
horas= int(input())
valor_hora= float(input())
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(n_f,(horas * valor_hora)))