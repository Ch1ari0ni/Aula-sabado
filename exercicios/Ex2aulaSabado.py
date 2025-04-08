soma_pares = int() #DECLARE soma_pares COMO INTEIRO
soma_impares = int() #DECLARE soma_impares COMO INTEIRO
numero = int() #DECLARE numero COMO INTEIRO

soma_pares += 0 #soma_pares ← 0
soma_impares += 0 #soma_impares ← 0

numero = int(input("Digite um número positivo para classificar (ou um número negativo para sair): "))

while numero >= 0: #ENQUANTO numero >= 0 FAÇA

    if (numero % 2 == 0): #SE numero MÓDULO 2 = 0 ENTÃO
        soma_pares += numero #soma_pares ← soma_pares + numero
        print("Número ", numero, " é PAR.") #EXIBA "Número ", numero, " é PAR."
        
    else:
        soma_pares += soma_impares + numero #soma_impares ← soma_impares + numero
        print("Número ", numero, " é IMPAR.") #EXIBA "Número ", numero, " é ÍMPAR."
            
    numero = int(input("Digite outro número (ou um número negativo para sair): "))

print("Processo encerrado.") #EXIBA "Processo encerrado."
print("Soma total dos números PARES: ", soma_pares) #EXIBA "Soma total dos números PARES: ", soma_pares
print("Soma total dos números ÍMPARES: ", soma_impares) #EXIBA "Soma total dos números ÍMPARES: ", soma_impares