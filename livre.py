from media import Media
class Livre(Media):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self._auteur = auteur
    def transforme(self):
        return {"Livre":self._titre, "Année" :self._annee, "Auteur" :self._auteur}
    def afficher(self):
        return f"Livre : {self._titre} - Année : ({self._annee}) - Auteur : {self._auteur}"