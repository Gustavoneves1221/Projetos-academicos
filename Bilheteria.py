ticket_int = 30.00
ticket_half = 15.00
pipoca = 20.00
refri = 10.00

print ('\ningresso = R$30,00\npipoca = R$20,00 \nrefrigerante = R$10,00\n')
ticket_comp = int(input('Quantos ingressos você deseja comprar?: '))
halfticket_comp = int(input('Quantos ingressos são meia-entrada?: '))
pipoca_comp = int(input('Quantas pipocas você deseja comprar?: '))
refri_comp = int(input('Quantos refrigerantes você deseja comprar?: '))

desconto = halfticket_comp * (ticket_int/2)

print(f'\nVocê recebeu um desconto de R${desconto:.2f} por ter comprado {halfticket_comp} ingressos de meia-entrada\n')

total_ticket = (ticket_int * ticket_comp)
total_pipoca = (pipoca * pipoca_comp)
total_refri = (refri * refri_comp)

sub_total = (total_ticket + total_pipoca + total_refri) - desconto

if pipoca_comp == 1 and refri_comp == 1:
    print('\nVocê recebeu um desconto de R$5,00 por ter comprado 1 pipoca e 1 refrigerante juntos!\n')
    sub_total = sub_total - 5

print(f'O total da compra é R${sub_total:.2f}\n')
print('Cobramos uma taxa de conveniencia de 5%')

total_taxa = sub_total * 1.05

print(f'\nO total da compra com a taxa de conveniencia é R${total_taxa:.2f}\n')

pessoas = int(input('Você gostaria de dividir a compra em quantas pessoas?: \n'))

while True:
    if pessoas <= 0:
        print('\nO número de pessoas deve ser maior que 0!\n')
        pessoas = int(input('Você gostaria de dividir a compra em quantas pessoas?: \n'))
    else:
        break

total_def = total_taxa / pessoas

if total_def < 120.00:
    print('\nSua compra esta saindo acima do valor mediado!')

print(f'\nO total da compra dividido entre {pessoas} pessoas é R${total_def:.2f}\n')
print('\n=============== RECIBO ===============')
print(ticket_comp,f' Ingressos     = R${total_ticket:.2f}')
print(pipoca_comp,f' Pipocas       = R${total_pipoca:.2f}')
print(refri_comp,f' Refrigerantes = R${total_refri:.2f}')
print(f'\nTotal = R${total_taxa:.2f}')
print('\nSua compra foi Finalizada!')
