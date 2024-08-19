#Area= Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura., b) a área do círculo de raio C. (pi = 3.14159),c) a área do trapézio que tem A e B por bases e C por altura.,d) a área do quadrado que tem lado B.,e) a área do retângulo que tem lados A e B.
try:
    a, b, c= map(float,input().split())

    print('TRIANGULO: {:.3f}'.format(0.5 * a * c ))
    print('CIRCULO: {:.3f}'.format(3.14159 * (c**2)))
    print('TRAPEZIO: {:.3f}'.format(0.5 * (a+b)*c))
    print('QUADRADO: {:.3f}'.format(b**2))
    print('RETANGULO: {:.3f}'.format(a*b))

except ValueError as e:
    print('Erro: {}. Certifique-se de que os valores estão no formato correto'.format(e))

