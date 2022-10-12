def factorielle(nbr):
    fact = 1
    for i in range(1, nbr + 1):
        fact = fact * i
    print(nbr, '! = ', fact)

def demandeNombre():  # demande nombre
        nombre = input("Entre nombre non nul : ")
        try:
            nombreInt = int(nombre)

        except  ValueError:
            print("erreur Vous devez entre un nombre")
            return demandeNombre()

        return nombreInt


nombre = demandeNombre()
factorielle(nombre)


