a = 3
b = 4

a%2 == 0 and b%2 == 0 # Erreur, seulement True quand les 2 sont pairs

(a%2 == 0 and b%2 == 0) or (a%2 == 1 and b%2 == 1) # OK 


a%2 == b%2 # OK
