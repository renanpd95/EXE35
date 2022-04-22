import math,os

n1 = int(input("Digite um numero:"))
os.system('clear')
unidade =  n1%10
div1 = n1/10

dezena = div1%10
div2 = div1/10

centena = div2%10
milhar = div2/10

milhar = math.floor(milhar)
centena = math.floor(centena)
dezena = math.floor(dezena)

print("Milhar: ",milhar,"Centena: ",centena,"Dezena: ",dezena,"Unidade: ",unidade)
