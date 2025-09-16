from media import Media
class Film(Media):
    def __init__(self, titre, annee, realisateur):
        super().__init__(titre, annee)
        self._realisateur = realisateur
    def transforme(self):
        return {"Film":self._titre, "Année" :self._annee, "Réalisateur" :self._realisateur}
    def afficher(self):
        return f"Film: {self._titre} - Année : ({self._annee}) - Réalisateur: {self._realisateur}"