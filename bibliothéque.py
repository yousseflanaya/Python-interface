from media import Media
class Bibliotheque:
    def __init__(self):
        self.medias = {}
    def ajouter_media(self, m):
        titre=m.get_titre() #get_titre hiya method kayna f class Media
        self.medias[titre]=m
    def supprimer_media(self, titre):
        titre_sup=titre.lower()
        if titre_sup in self.medias :
            del self.medias[titre_sup]
    def rechercher_media(self, titre):
        titre_recherch=titre.lower()
        resultat = []  
        for m in self.medias.values():
         if titre_recherch in m.get_titre():  
          resultat.append(m)  
          return resultat  
    def get_tous_medias(self):
        return list(self.medias.values())