### IF
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

###

quantidade = 10  
preço = 20 

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

### FOR 
for i in range(2,6):
    print(i)

lista_alunos = ["Rafael", "Ana", "Carlos"]
for aluno in lista_alunos:
    print(aluno)