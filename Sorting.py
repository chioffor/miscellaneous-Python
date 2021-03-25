"""
Chika Offor
Cwiczenie 62-4
Program wypisze sortowane numerow rosnaco z lista numerow podane przez uzytkownika
"""

def sorta(list_numerow):            #funkcja ktora sortuje numerow
    sortowane_list = []
    while list_numerow:
        minimum = list_numerow[0]
        for numer in list_numerow:
            if numer < minimum:
                minimum = numer
        sortowane_list.append(minimum)
        list_numerow.remove(minimum)
    return sortowane_list

list_numerow = []
print("Prosze podac numer calkowitych, zeby zobaczyc result, prosze podac '0'")
while True:
    numer = int(input("Prosze podac numer calkowity: "))
    if numer == 0:
        break
    list_numerow.append(numer)

x = sorta(list_numerow)
print(x)
