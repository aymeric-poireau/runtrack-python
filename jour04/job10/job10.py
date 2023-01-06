def tableau(liste):
    produit = 0
    for i in range(len(liste)):
        if(25 < liste[i] < 90): #Elle regarde  si liste[i] est entre 25 et 90
            if(produit == 0):
                produit = produit + liste[i]
            else:
                produit *= liste[i]
    return(produit)

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(tableau(L))
