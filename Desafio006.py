#Desafio 1 Crie um programa que leia dos numeros e some
print("Vamos somar..\n")
num1 = int(input("Digite o primeiro numero \n"))
num2 = int(input("Digite o segundo numero  \n"))
soma = num1+num2
print("A soma entre {} e {}  é igual a {}".format(num1, num2, soma))

#Desafio 2 Cria um programa que leia o input e mostre na tela o tipo
algo = input("Digite alguma coisa \n")
print("o tipo primitivo é {}".format(type(algo)))
print("está vazio ? {}".format(algo.isspace()))
print("é alfa numérico...", algo.isalnum())
print("é numérico...", algo.isnumeric())
print("é alfa ?",algo.isalpha())
