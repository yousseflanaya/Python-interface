#kan3ayto 3la module dyal tkinter
from tkinter import *
from tkinter import ttk

#kan3ayto 3la ga3 les modules li 3andna
from bibliothéque import Bibliotheque
from livre import Livre
from film import Film
from musique import Musique
from souvegarder import sauvegarder, charger

#kan'créiw window bach ytra l'affichage f wa7ed l fenétre
window = Tk()
window.geometry("850x650")
window.title("Naoufal and Youssef and Yasser Media Library")
window.configure(bg="#f0f0f0")

#kan3ayto 3la class Bibliotheque katkon 5awiya w methode charger() men module sauvegarder()
biblio = Bibliotheque()
datas = charger()

#hadi loop bach ytra save l ga3 les infos li déja kaynin f fichier JSON bach n9adro nbaynohom
for data in datas:
    type_media = data.get("type")
    titre = data.get("titre")
    annee = data.get("annee")
    if type_media == "livre":
        media = Livre(titre, annee, data.get("auteur"))
    elif type_media == "film":
        media = Film(titre, annee, data.get("realisateur"))
    elif type_media == "musique":
        media = Musique(titre, annee, data.get("artiste"))
    else:
        continue
    biblio.ajouter_media(media)

#StringVar() hiya fonction prédéfinie li kat5alina n jahhzo les variables bach ya5do les valeurs li kaydo5lo lina fles inputs (entries)
type_var = StringVar()
titre_var = StringVar()
annee_var = StringVar()
last_var = StringVar()

#hadi fonction katbadel l label la55er dyal les medias 3la 7sseb ina media 5tarina
def update_specifique_label(*args):
    type_selected = type_var.get()
    label_map = {
        "livre": "Auteur",
        "film": "Réalisateur",
        "musique": "Artiste"
    }
    last_label.config(text=label_map.get(type_selected))

# création dyal label "Type de média" w l Combobox dyalha (Select li f html)
Label(text="Type de média :", bg="#f0f0f0", font=("Arial", 10, "bold")).pack()
type_combo = ttk.Combobox(textvariable=type_var, state="readonly")
type_combo['values'] = ("livre", "film", "musique")
type_combo.current(0)
type_combo.pack(pady=5)
type_var.trace("w", update_specifique_label)

#création Frame fin ghadi njem3o l entries b labels dyalhom (nefss lconcept dyal div wla form f html)
entry_frame = Frame(window, bg="#f0f0f0")
entry_frame.pack(pady=10)

                                   #création dyal kol entry 9odam l label dyalha
#création dyal label "Titre :" w entry dyalo
Label(entry_frame, text="Titre :", bg="#f0f0f0").grid(row=0, column=0,  padx=5, pady=3)
entry_titre = Entry(entry_frame, textvariable=titre_var, width=30).grid(row=0, column=1, padx=5, pady=3)

#création dyal label "Année :" w entry dyalo
Label(entry_frame, text="Année :", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=3)
entry_annee = Entry(entry_frame, textvariable=annee_var, width=30).grid(row=1, column=1, padx=5, pady=3)

#création dyal last label (par défaut ghaykon "Auteur") w entry dyalo
last_label = Label(entry_frame, text="Auteur", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=3)
last_entry = Entry(entry_frame, textvariable=last_var , width=30).grid(row=2, column=1, padx=5, pady=3)

#création dyal label "Résultat :" w entry dyalo
Label(window, text="Résultat :", bg="#f0f0f0", font=("Arial", 10, "bold")).pack()
result_text = Text(window, height=15, width=90, bg="#ffffff", fg="#000000", font=("Courier", 9))
result_text.pack(pady=10)

# hadi methode li biha kan5wiw l entries bach n9edro nzido chi media jdida (nefss lconcept dyal .reset() f JS)
def clear_fields():
    titre_var.set("")
    annee_var.set("")
    last_var.set("")

# hadi methode ghan7tajouha fach ghandiro click 3la l button dyal "Afficher tous"
def afficher_medias():
    result_text.delete(1.0, END) #had ster ghan7tajouh bach n5wiw ltext area fin ghaybano lina les messages w les résultats
    medias = biblio.get_tous_medias()
    if not medias:
        result_text.insert(END, "Aucun média dans la bibliothèque.\n")
    else:
        for m in medias:
            result_text.insert(END, m.afficher() + "\n")

# hadi methode ghan7tajouha fach ghandiro click 3la l button dyal "Rechercher"
def rechercher_media():
    result_text.delete(1.0, END)
    titre = titre_var.get().strip()
    if not titre:
        result_text.insert(END, "Veuillez entrer un titre.\n")
        return
    resultats = biblio.rechercher_media(titre)
    if not resultats:
        result_text.insert(END, "Aucun résultat trouvé.\n")
    else:
        for m in resultats:
            result_text.insert(END, m.afficher() + "\n")

# hadi methode ghan7tajouha fach ghandiro click 3la l button dyal "Suprimer"
def supprimer_media():
    result_text.delete(1.0, END)
    titre = titre_var.get().strip()
    if not titre:
        result_text.insert(END, "Veuillez entrer un titre à supprimer.\n")
        return
    else:
     biblio.supprimer_media(titre)
     sauvegarder(biblio.medias)
     result_text.insert(END, f"'{titre}' supprimé.\n")

# hadi methode ghan7tajouha fach ghandiro click 3la l button dyal "Ajouter "
def ajouter_media():
    result_text.delete(1.0, END)
    type_media = type_var.get()
    titre = titre_var.get().strip()
    annee = annee_var.get().strip()
    last = last_var.get().strip()
    
# hada condition kaybazez 3la l'utilisateur y3amer ga3 les champs
    if not titre or not annee or not last:
        result_text.insert(END, "Veuillez remplir tous les champs.\n")
        return

# hna kant2akdo wach l'année li da5el l'utilisateur wach chiffre wla fiha des lettres
    try:
        annee = int(annee)
    except ValueError:
        result_text.insert(END, "Année invalide.\n")
        return

# kan5aliw lprogram y5dem b ay class 3la 7sseb choie dyal l'utilisateur fel'combobox 
    if type_media == "livre":
        media = Livre(titre, annee, last)
    elif type_media == "film":
        media = Film(titre, annee, last)
    elif type_media == "musique":
        media = Musique(titre, annee, last)

# hna kaytra l'ajout dyal lmedia li zad l'utilisateur
    biblio.ajouter_media(media)

# kan3ayto 3la methode sauvegarder() bach ytra save ldictionnaire self.medias li kayn f class Bibliothéque f fichier JSON
    sauvegarder(biblio.medias)
    result_text.insert(END, f"{type_media.capitalize()} ajouté avec succès.\n")
    clear_fields()

# création dyal Frame (div f html)
btn_frame = Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=10)
# style dyal l buttons
ajouter_style = {
    "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049",
    "font": ("Arial", 10, "bold"), "width": 15
}
afficher_style = {
    "bg": "#2196F3", "fg": "white", "activebackground": "#1976D2",
    "font": ("Arial", 10, "bold"), "width": 15
}
rechercher_style = {
    "bg": "#FF9800", "fg": "white", "activebackground": "#FB8C00",
    "font": ("Arial", 10, "bold"), "width": 15
}
supprimer_style = {
    "bg": "#F44336", "fg": "white", "activebackground": "#D32F2F",
    "font": ("Arial", 10, "bold"), "width": 15
}

# kanrebto kol button bel function dyalha w style dyalha
Button(btn_frame, text="Ajouter", command=ajouter_media, **ajouter_style).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Afficher Tous", command=afficher_medias, **afficher_style).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Rechercher", command=rechercher_media, **rechercher_style).grid(row=0, column=2, padx=10)
Button(btn_frame, text="Supprimer", command=supprimer_media, **supprimer_style).grid(row=0, column=3, padx=10)

# fonction prédéfinie mohima bzaf bach ytra éxécution ll interface
window.mainloop()