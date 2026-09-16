opc1 = 42.00
opc2 = 36.50
opc3 = 58.00
opc4 = 38.00

print("prato 1 = ", opc1)
print("prato 2 = ", opc2)
print("prato 3 = ", opc3)
print("prato 4 = ", opc4)

preco_uni = float(input("\nDIgite o preço do item: "))
quant = int(input("Digite a quantidade desejada: "))
valor_total = preco_uni * quant
valor_def = valor_total * 1.10

print("\nvalor total: ", valor_total)

print("\nCobramos uma taxa de 10% sobre o valor total")
print(f"\nO Total ficou igual a: {valor_total:.2f32}")

div_conta = float(input("\nem quantas pessoas a conta sera dividida?: "))

conta = valor_def / div_conta

print(f"A conta ficou igual a: {conta:.2f}\n")

resposta = input("Você deseja doar uma gorjeta? (sim/não): ")
resposta_ajustada = resposta.lower().strip()

if resposta_ajustada == "sim":
    print("Ótimo! Vamos continuar.")
    float(input("\nQuanto você gostaria de deixar?: "))
    print("Obrigado por sua contribuição!")
elif resposta_ajustada == "não" or resposta_ajustada == "nao":
    print("Entendido. Encerrando o programa.")
else:
    print("Resposta inválida! Por favor, digite 'sim' ou 'não'.")


