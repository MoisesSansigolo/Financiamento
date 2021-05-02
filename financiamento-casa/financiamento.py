casa = float(input('Qual o valor da casa R$ '))
sálario = float(input('Qual o salario do comprador R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = sálario * 30 / 100 
print('Para financiar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO')
else:
    print('Empréstimo \033[31mNEGADO') 