import os

# Définissez le chemin vers votre dossier 'data'
dossier_data = "./data"

# Définissez le nom du fichier de sortie
fichier_sortie = "documentation_nextjs_concatenee.txt"

# Créez ou ouvrez le fichier de sortie
with open(fichier_sortie, "w", encoding="utf-8") as sortie:
    # Parcourez chaque fichier dans le dossier
    for fichier in os.listdir(dossier_data):
        chemin_fichier = os.path.join(dossier_data, fichier)

        # Assurez-vous qu'il s'agit d'un fichier texte
        if os.path.isfile(chemin_fichier) and fichier.endswith(".txt"):
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                contenu = f.read()

                # Écrivez le contenu du fichier dans le fichier de sortie
                sortie.write(contenu + "\n\n")

print("La fusion des fichiers est terminée.")
