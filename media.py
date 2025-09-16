class Media:
    def __init__(self, titre, annee):
        self._titre = titre
        self._annee = annee
    def get_titre(self):
        return self._titre
    def set_titre(self,new_titre):
        self._titre=new_titre
    def transforme(self):
        return {"Titre" : self._titre, "Année" : self._annee}
    def afficher(self):
        return f"Titre : {self._titre} - Année : ({self._annee})"