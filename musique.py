from media import Media
class Musique(Media):
    def __init__(self, titre, annee, artiste):
        super().__init__(titre, annee)
        self._artiste = artiste
    def transforme(self):
        return {"Musique":self._titre, "Année" :self._annee, "Artiste" :self._artiste}
    def afficher(self):
        return f"Musique : {self._titre} - Année : {self._annee} - Artiste: {self._artiste} "