from pathlib import Path
import re

# Chemin vers le dossier contenant les fichiers
chemin = Path("D:/Utilisateur/Downloads/Video")
# Liste tous les fichiers dans le dossier
fichiers = [f for f in chemin.iterdir() if f.is_file()]

# Parcourt chaque fichier dans le dossier
for fichier in fichiers:
    mot_a_chercher = re.compile(r'remplace par le saison ou le titre du film ou serie à réchercher', re.IGNORECASE)
    
    def nettoyer_nom(nom):
        return re.sub(r'[<>:"/\\|?* _.-@()]','',nom)
    
    correct  =  mot_a_chercher.search(fichier.name)
    # Vérifie si le mot est trouvé dans le nom du fichier
    if correct:
        
        saison = correct.group(0)
        
        #nom du dossier à créer
        nom_emplacement = chemin / nettoyer_nom(f"remplace par nom_dossier à créer") 
        nom_emplacement.mkdir(exist_ok=True)
        
        # Déplace le fichier dans ce dossier
        fichier.rename(nom_emplacement / fichier.name)
        print(f"Déplacé : {fichier.name} -> {nom_emplacement}")
    else:
        print(f"Mot non trouvé dans : {fichier.name}")