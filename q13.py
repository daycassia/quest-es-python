# Esfera: Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
raio= float(input())
volume= (4/3.0)* 3.14159 * (raio**3)
print(f'VOLUME = {volume:.3f}')
