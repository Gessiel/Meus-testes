# Xuser Produções

#coding UTF-8

print(" Notas Escolares.... ")

print("")

Bimestre1 = float(input(" Resultado do 1º Bimestre, "))
print(" Obrigado...")              
Bimestre2 = float(input(" Resultado do 2º Bimestre, "))
print(" Obrigado...")             
Bimestre3 = float(input(" Resultado do 3º Bimestre, "))
print(" Obrigado...")              
Bimestre4 = float(input(" Resultado do 4º Bimestre, "))
print(" Obrigado...")
                   
print("")

Valores = Bimestre1 + Bimestre2 + Bimestre3 + Bimestre4

print("")

print(" Você ficou com: %.2f" %Valores," Pontos..." )

if(Valores >= 60):
                print("")
                print(" Parabéns você foi aprovado... ")
else:
                if(Valores <= 59.9):
                    print("")
                    print(" Você foi reprovado... ")

print("")

Sair = input(" Pressione qualquer tecla para sair... ")
