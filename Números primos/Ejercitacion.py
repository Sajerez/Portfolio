def num_primo (largo):                  #Definimos la función, llamada "num_primo", con parámetro "largo"
    primos = [2]                        #Armamos una lista de números primos que contiene al primero de ellos (2)
    numero = 1                          #Definimos que "numero", es decir, nuestro dividendo, vale uno (1)
    while largo>len(primos):            #Armamos un loop: mientras la longitud de la lista "primos" sea menor al parámetro "largo", se repetirá lo siguiente:
        numero=numero+1                 #Sumamos una unidad a "numero"
        for i in primos:                #Recorremos la lista de primos con el elemento iterable "i", siendo "i" nuestro divisor
            if numero%i==0:             #Si "numero" dividido "i" tiene resto 0 (cero), entonces sabemos que NO es primo y por tanto:
                break                   #rompemos el bucle y volvemos al incio del loop. Sino pasamos a la siguiente condición:
            elif i>=numero**0.5:        #si "i" es mayor o igual a la raiz de "numero", entonces encontramos un número primo. Entendiendo que la raiz cuadrada es el limite de verificación dado que no es necesario chequear todos los divisores acorde a la teoría de los factores en pares.
                primos.append(numero)   #Añadimos el número primo a la lista
                break                   #Cortamos el bucle y proseguimos el loop con el siguiente número
    return primos[-1]                   #La función nos devuelve el último número primo de la lista "primos" (aquel que fue solicitado)


