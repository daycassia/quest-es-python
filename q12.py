#Calculo simples: Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
try:
    # Leitura dos dados das peças
    dados_peca1 = input().split()
    dados_peca2 = input().split()

    # Extração dos valores para a peça 1
    cod_peca1 = int(dados_peca1[0])
    n_peca1 = int(dados_peca1[1])
    valor_peca1 = float(dados_peca1[2])

    # Extração dos valores para a peça 2
    cod_peca2 = int(dados_peca2[0])
    n_peca2 = int(dados_peca2[1])
    valor_peca2 = float(dados_peca2[2])

    # Cálculo do valor total a ser pago
    valor_total = (n_peca1 * valor_peca1) + (n_peca2 * valor_peca2)

    # Exibição do valor total formatado
    print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

except ValueError as e:
    print(f"Erro: {e}. Certifique-se de que os valores estão no formato correto.")


