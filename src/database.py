class personne :
    def __init__(self, name: str, age: int):

class professeur(personne):
    def __init__ (self, courses: list):
        pass

class etudiant(personne):
    def __init__(self, matricule: str, moyenne: float):
        pass