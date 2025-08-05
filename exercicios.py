#Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1= int(input("Insira um  um numero inteiro: "))
numero_2= int(input("Insira outro numero inteiro: "))
soma = numero_1+numero_2
print("A soma dos numéros é : ", soma)


#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um numero: "))
resto_divisao = numero%5
print("o resto da divisão é :", resto_divisao)

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1= int(input("Insira um  um numero inteiro: "))
numero_2= int(input("Insira outro numero inteiro: "))
multiplicacao = numero_1 * numero_2
print("A multiplicação é : ", multiplicacao)


#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_1= int(input("Insira um  um numero inteiro: "))
numero_2= int(input("Insira outro numero inteiro: "))
divisao_inteira  = numero_1//numero_2
print("o resultado da divisão inteira é  :", divisao_inteira)


#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um numero: "))
quadrado = numero**2
print(" O quadrado do numero :", numero , "é: ", quadrado)

#Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input("Digite um numero decimal: "))
numero_2 = float(input("Digite outro um numero decimal: "))
soma = numero_1 + numero_2
print(" A soma desses numeros é: ", soma)

#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Digite um numero decimal: "))
numero_2 = float(input("Digite outro um numero decimal: "))
media = (numero_1+numero_2)/2
print("A Média dos números é: ", media)

#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input("Digite um numero base decimal: "))
numero_expoente = float(input("Digite outro um numero expoente decimal: "))
potencia = numero_base ** numero_expoente
print(" A Potência é : ", potencia)

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura_celsius = float(input("Digite a temperatura em Graus Celsius: "))
temperatura_fare = (temperatura_celsius*9/5)+32
print("A temperatura em Fahrenheit é :", temperatura_fare)

#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada
raio = float(input("Digite o raio do círculo: "))
area_do_circulo = 3.14 * raio**2
print("A área do circulo é :", area_do_circulo)

#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Digite o seu nome: ")
nome_maiusculo = nome.upper()
print("O nome maísuculo é : ", nome_maiusculo)

#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite o seu nome: ")
nome_minusculo = nome.lower()
print("O nome minísculo é : ", nome_minusculo)

#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
resultado = frase.strip()
print("A frase corrigida é :", resultado)

#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato: dd/mm/aaaa")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

#Escreva um programa que concatene duas strings fornecidas pelo usuário.
frase_1 = input("Digite uma frase: ")
frase_2 = input("Digite uma outra frase: ")
resultado = frase_1 + ',' + frase_2
print(resultado)

#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
exp1 = input("Digite True ou False: ")
exp2 = input("Digite True ou False: ")
# Converte strings para booleanos
bool1 = exp1.lower() == "true"
bool2 = exp2.lower() == "true"
resultado = bool1 and bool2
print("O resultado é:", resultado)

