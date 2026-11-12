def afficher_menu():
    print("\n*** GESTION DES TÂCHES ***")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")

def ajouter_tache(liste_taches):
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre de la tâche ne peut pas être vide.")
    else:
        liste_taches.append(titre)
        print("Tâche ajoutée avec succès.")

def afficher_taches(liste_taches):
    if len(liste_taches) == 0:
        print("Aucune tâche enregistrée pour le moment.")
    else:
        print("\n*** Liste des tâches ***")
        for i in range(len(liste_taches)):
            print(f"{i + 1}. {liste_taches[i]}")

def rechercher_tache(liste_taches):
    if len(liste_taches) == 0:
        print("La liste est vide, impossible de rechercher.")
        return

    mot_cle = input("Entrez un mot-clé à rechercher : ").strip().lower()
    if mot_cle == "":
        print("Erreur : veuillez saisir un mot-clé valide.")
        return

    trouve = False
    print(f"\n *** Résultats pour '{mot_cle}' ***")
    for i in range(len(liste_taches)):
        if mot_cle in liste_taches[i].lower():
            print(f"{i + 1}. {liste_taches[i]}")
            trouve = True

    if not trouve:
        print("Aucune tâche ne correspond à votre recherche.")

def main():
    taches = []
    continuer = True

    while continuer:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            rechercher_tache(taches)
        elif choix == "0":
            print("Fermeture du programme. À bientôt !")
            continuer = False
        else:
            print("Erreur : option invalide. Veuillez choisir 1, 2, 3 ou 0.")

if __name__ == "__main__":
    main()