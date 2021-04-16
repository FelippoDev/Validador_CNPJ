# Validador_CNPJ
Algoritmo criado em Python para a validação de CNPJ. Cheque a página [macoratti.net](http://www.macoratti.net/alg_cnpj.htm) para um entendimento sobre o método necessário para a verificação de um CNPJ. 



Neste início do codigo temos a entrada de dados e o tratamento do mesmo. checamos dentro de cada iteração se o valor em x é numérico, sendo numérico será adicionado a lista `v1` e a cada volta do laço será somado 1  a varíavel  `count`.
```python
count = 0
v1 = []
list_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj = str(input('Digite o CNPJ: '))
for x in cnpj:
    if x.isnumeric():
        if count < 12:
            count += 1
            v1.append(int(x))
```

Será checado na condição, se o valor contido na varíavel `count` é menor que 12,o CNPJ será invalido, caso contrário, será feita a junção dos itens contidos nas listas `v1` e `list_1`, sendo `list_1` a lista  que conterá os valores fixos necessários para a validação de um CNPJ e a lista  `v1` o CPNJ informado pelo user que iremos checar se é valido ou não.
```python
if count < 12:
    print('CNPJ invalido!')
else:
    conjunto_1 = list(zip(v1, list_1))
```

Logo após a junção da lista `v1` com a lista `list_1` será realizado a multiplicação de cada dupla de número formado após a junção destes pelo comando `zip()`, o resultado será guardado dentro da lista `val_1`. Contido os novos valores na lista `val_1` irá ser feito a soma total destes valores e dividido por 11 sendo guardado o resto desta divisão, substítuindo os valores que antes estavam guardados nesta lista. Por fim, uma condição irá checar se o valor contido em `val_1` é maior que 2, se for maior será subtraído por 11 se não o valor contido na varíavel `val_1` será 0.
```python
 val_1 = [a * b for (a, b) in conjunto_1]
    val_1 = sum(val_1) % 11
    if val_1 > 2:
        val_1 = 11 - val_1
    else:
        val_1 = 0
```
Na lista `list_2` temos o mesmo valor contido na `lista_1` só que adicionado o número 6 ao seu primeiro índice.Temos a lista `val_2` sendo uma cópia da lista `v1` e sendo adicionado nela o primeiro digíto verificador, logo adiante, temos a lista `conjunto_2` contendo a junção da lista `val_2` e `list_2`.  
```python
  list_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    val_2 = v1[:]
    val_2.append(val_1)
    conjunto_2 = list(zip(val_2, list_2))
```


Ao final do código temos a `val_2` recebendo o produto da multiplicação das listas `val_2` e `list_2`, em seguida, recebendo o resto da divisão por 11 da soma total dos valores contidos nela. Caindo, então, na condição de que se o valor contido em `val_2` for maior que 2 então será subtraído por 11 se não o segundo digíto de verificação do CNPJ será igual a 0.
Temos no último trecho do código a checagem se os dois ultimos digítos do CPNJ informado pelo user é igual ao dois digítos acho pela formúla de validação de CNPJ. Se for igual o CNPJ será valido se não o CNPJ será invalido. 
```python
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

```


## Contribuidores
@[FelippoDev](https://github.com/FelippoDev)