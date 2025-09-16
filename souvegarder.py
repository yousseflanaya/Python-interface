from media import Media
import json
# hadi methode ghadir sauvegarder l les infos dyal les medias f fichier json 
def sauvegarder(medias_dict, nom_fichier="media.json"):
    liste_dicts = []
    for m in medias_dict.values():
        d = m.transforme()
        d['type'] = m.__class__.__name__ 
        liste_dicts.append(d)
    with open(nom_fichier, "w") as f:
        json.dump(liste_dicts, f, indent=4)
#hadi methode li n9edro biha n9ra ach kayn west fichier json
def charger(nom_fichier="media.json"):
    try:
        with open(nom_fichier, "r") as f:
            Liste = json.load(f)
        return Liste
    except FileNotFoundError:
        return []
