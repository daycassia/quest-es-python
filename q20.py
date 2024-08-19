#Cédulas: Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
try: 
    def calcular_notas(valor):
        notas=[100,50,20,10,5,2,1]
        quantidade_notas= {}
        for nota in notas:
            if valor >= nota:
                quantidade= valor // nota
                quantidade_notas[nota]=quantidade
                valor -=quantidade*nota
            else:
                quantidade_notas[nota]=0
        return quantidade_notas
    def imprimir_resultado( valor, quantidade_notas):
        print(valor)
        for nota in [100,50,20,10,5,2,1]:
            print(f'{quantidade_notas[nota]} nota(s) de R${nota},00')
    valor= int(input().strip())
    quantidade_notas= calcular_notas(valor)
    imprimir_resultado(valor, quantidade_notas)
except ValueError as e:
    print(f'Erro: {e}. Certifique-se de que a entrada é um número inteiro.')
