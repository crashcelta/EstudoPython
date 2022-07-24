def saudacao(msg, nome):
    print(msg, nome)
saudacao('olá', 'Jota')
#############################################
def adicao(n1, n2, n3):
    print(n1+n2+n3)
adicao(3, 4, 6)
##############################################
def aumento(n1, n2):
    porc = n1*(n2/100)
    return f'{n1 + porc:.2f}'
aumento = aumento(1000, 20)
print(aumento)
##############################################
def FizzBuzz(n1):
    if n1%5 == 0 and n1%3 == 0:
        return 'FizzBuzz'
    if n1%5 == 0:
        return 'buzz'
    if n1%3 == 0:
        return 'fizz'
valor = FizzBuzz(6)
print(valor)




