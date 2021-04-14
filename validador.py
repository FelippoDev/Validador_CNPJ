print('<<<< VALIDADOR DE CNPJ >>>>')
count = 0
v1 = []
list_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj = str(input('Digite o CNPJ: '))
for x in cnpj:
    if x.isnumeric():
        if count < 12:
            count += 1
            v1.append(int(x))
if count < 12:
    print('CNPJ invalido!')
else:
    conjunto_1 = list(zip(v1, list_1))
    val_1 = [a * b for (a, b) in conjunto_1]
    val_1 = sum(val_1) % 11
    if val_1 > 2:
        val_1 = 11 - val_1
    else:
        val_1 = 0

    list_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    val_2 = v1[0:]
    val_2.append(val_1)
    conjunto_2 = list(zip(val_2, list_2))
    val_2 = [a * b for (a, b) in conjunto_2]
    val_2 = sum(val_2) % 11
    if val_2 > 2:
        val_2 = 11 - val_2
    else:
        val_2 = 0

    if (str(val_1) + str(val_2)) == cnpj[-2:]:
        print('CNPJ valido!')
    else:
        print('CNPJ invalido!')
