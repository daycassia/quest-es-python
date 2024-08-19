#Distancia entre dois pontos: Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:
#Distancia= sqrt(((x2-x1)**2)+((y2-y1)**2))
from math import sqrt
try:
    x1, y1=map(float, input().split())
    x2, y2=map(float,input().split())
    distancia= sqrt(((x2-x1)**2)+((y2-y1)**2))
    print(f'{distancia:.4f}')
except ValueError as e:
    print(f'Erro: {e}. Certifique-se de que os valores estão no formato correto')