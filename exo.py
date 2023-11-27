def fonction(n): # Définir la fonction
    if n == 0: # On retourne le cas basique si n == 0
        return -2 
    else: # Sinon, on calcule la suite
        suites = [-2] # 3 Déclarer une liste dont le premier élément est -2
        for _ in range(n - 1): # Dans chaque élément de la liste
            suites.append(suites[-1] ** 2 - 1) # On ajoute à la liste le résultat du calcul fait dans append().
        return suites # On retourne le résultat final
    
print(fonction(10))

