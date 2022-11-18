from replit import clear
from art import logo
#Calculadora

#adção
def add(n1 , n2):	
	return n1 + n2

#subtração
def subtr(n1, n2):	
	return n1 - n2

#mutiplicação
def mult(n1,n2):	
 	return n1 * n2

#divisão
def divi(n1,n2): 
	return n1 / n2


operadores = {
	"+": add,
	"-": subtr,
	"*": mult,
	"/": divi

}

def calculadora():
	print(logo)


num1 = int(input("Insira o Primeiro Numero: "))
for simbolo in operadores:
	print(simbolo)
	deve_continuar = True

while deve_continuar:	
		operador_simbolo = input("Escolha uma operação na linha acima: ")	
		num2 = float(input("Insira o Segundo Numero: "))	
		calculadora_function = operadores[operador_simbolo]
		resposta = calculadora_function(num1, num2)

		print(f"{num1} {operador_simbolo} {num2} = {resposta}")
	
		if input(f"Digite 's' para continuar calculando com {resposta}, or escolha 'n' para iniciar outro calculo") == "s":
			num1 = resposta
		else:
			deve_continuar= False
			clear()
			calculadora()

calculadora()


