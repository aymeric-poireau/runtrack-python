def list(liste):  #déclaration de la fonction et du paramètre
    for i in range(len(liste)): #boucle for in
        liste[i] += 1  #incrémentation
    return(liste) #retourner le paramètree

L = [7, 11, 42, 39, 2] #tableau et liste de numéro

print(list(L)) 
