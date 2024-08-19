#O Maior: Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
# MaiorAB: (a+b+abs(a-b))/2. Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
try:
    a, b, s= map(int, input().split())
    maiorab= (a+b+abs(a-b))/2
    if maiorab < s:
        print('{:.0f} eh o maior'.format(s))
    else:
        print('{:.0f} eh o maior'.format(maiorab))
except ValueError as e:
    print('Erro: {}. Certifique-se de que os valores estão no formato correto'.format(e))