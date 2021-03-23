import FunçõesDeEspalhamento as FDE

print("---------------- Exercicio DIVISÃO A ----------------")

funcao = FDE.divisão(12, range(0,101)) #Exercicio DIVISÃO A
print(funcao[3][1])

print("---------------- Exercicio DIVISÃO B ----------------")

funcao = FDE.divisão(11, range(0,101)) #Exercicio DIVISÃO B
print(funcao[3][1])

print("---------------- Exercicio DIVISÃO C ----------------")

funcao = FDE.divisão(97, range(1,10001)) #Exercicio DIVISÃO C
for item in funcao:
    print("{}, {}".format(item[0], len(item[1])))

#---------------------------------------------------------------------------------------------------------------

print("------------- Exercicio MULTIPLICAÇÃO A -------------")

funcao = FDE.multiplicacao(200, range(1,500001), 0.62) #Exercicio MULTIPLICAÇÃO A 
for item in funcao:
    print("{}, {}".format(item[0], len(item[1])))

print("------------- Exercicio MULTIPLICAÇÃO B -------------")

funcao = FDE.multiplicacao(200, range(1,500001),  0.61803398875) #Exercicio MULTIPLICAÇÃO B
for item in funcao:
    print("{}, {}".format(item[0], len(item[1])))

