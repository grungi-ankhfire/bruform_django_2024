class Personne():
    def __init__(self, nom):
        self.nom = nom

    def vous_faites_quoi(self):
        return f"{self.nom} ne fait rien."

    def comment_vous_vous_appelez(self):
        return f"Je m'appele {self.nom}."

# --- Solution commence ici

class Etudiant(Personne):
    def vous_faites_quoi(self):
        return f"{self.nom} fait son devoir."
        
# --- Tests

mary = Personne("Mary")
print(mary.comment_vous_vous_appelez())
print(mary.vous_faites_quoi())

betty = Etudiant("Betty")
print(betty.comment_vous_vous_appelez())
print(betty.vous_faites_quoi())
