
def ordenar(array,):
    for i in range(len(array)):#n
        for j in range(0,len(array)-1):#n
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array #n
array=[32,12,43,54]
print(array[1])
print(array[0])
array1=array
print(ordenar(array1))
""" Entonces en esta caso el Big(O) es n^2 tal que recoremos dos listas con los dos for
Omega=n  tal que recoremos la lista y luego devolvemos el array
Theta no existiria porque los grados son diferentes para big o y omega """