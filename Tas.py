 
import random

liste = random.sample(range(1, 100), 10)
print("Liste non triée :", liste)

def construire_tas(arr,n,i):
    plus_grand = i
    gauche = 2*i+1
    droit = 2*i+2

    if gauche < n and arr[gauche] > arr[plus_grand]:
        plus_grand = gauche

    if droit < n and arr[droit] > arr[plus_grand]:
        plus_grand = droit

    if plus_grand != i:
        arr[i], arr[plus_grand] = arr[plus_grand], arr[i]
        construire_tas(arr, n, plus_grand)

def tri_par_tas(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        construire_tas(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        construire_tas(arr, i, 0)

    return arr

liste_triee = tri_par_tas(liste[:])
liste_triee_decroissante = liste_triee[::-1]

print("Liste triée (décroissante) :", liste_triee_decroissante)
