#Consumo: Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
dist_total= int(input())
comb_total= float(input())
val= dist_total/comb_total
print('{:.3f} km/l'.format(val))