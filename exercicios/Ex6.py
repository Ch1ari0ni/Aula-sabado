pares = int() #DECLARE soma_pares COMO INTEIRO
impares = int() #DECLARE soma_impares COMO INTEIRO
numero = int(input("Digite um número inteiro: ")) #DECLARE numero COMO INTEIRO

pares += 0 #soma_pares ← 0
impares += 0 #soma_impares ← 0

while numero >= 0: #ENQUANTO numero >= 0 FAÇA

    if (numero % 2 == 0): #SE numero MÓDULO 2 = 0 ENTÃO
        pares += numero #soma_pares ← soma_pares + numero
        print("Número ", numero, " é PAR.") #EXIBA "Número ", numero, " é PAR."
        
    else:
        pares += impares + numero #soma_impares ← soma_impares + numero
        print("Número ", numero, " é IMPAR.") #EXIBA "Número ", numero, " é ÍMPAR."
            
    numero = int(input("Digite outro número inteiro: "))
