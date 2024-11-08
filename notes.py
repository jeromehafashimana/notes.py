
notes = []


def afficher_menu():
    print("\nMenu :")
    print("1. Ajouter une note")
    print("2. Afficher toutes les notes")
    print("3. Calculer la moyenne des notes")
    print("4. Supprimer une note")
    print("5. Quitter")


def ajouter_note():
    try:
        note = float(input("Entrez la note : "))
        notes.append(note)
        print("Note ajoutée avec succès.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def afficher_notes():
    if notes:
        print("Les notes actuelles :")
        for i, note in enumerate(notes, start=1):
            print(f"Note {i}: {note}")
    else:
        print("Aucune note à afficher.")


def calculer_moyenne():
    if notes:
        moyenne = sum(notes) / len(notes)
        print(f"La moyenne des notes est : {moyenne:.2f}")
    else:
        print("Aucune note pour calculer la moyenne.")


def supprimer_note():
    afficher_notes()
    try:
        index = int(input("Entrez le numéro de la note à supprimer : ")) - 1
        if 0 <= index < len(notes):
            notes.pop(index)
            print("Note supprimée avec succès.")
        else:
            print("Numéro de note invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


while True:
    afficher_menu()
    choix = input("Entrez votre choix : ")

    if choix == '1':
        ajouter_note()
    elif choix == '2':
        afficher_notes()
    elif choix == '3':
        calculer_moyenne()
    elif choix == '4':
        supprimer_note()
    elif choix == '5':
        print("Programme terminé.")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
