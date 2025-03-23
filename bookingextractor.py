import re

def extraire_identifiants(fichier_entree, fichier_sortie):
    with open(fichier_entree, 'r', encoding='utf-8', errors='ignore') as f_entree, \
         open(fichier_sortie, 'w', encoding='utf-8') as f_sortie:
        
        for ligne in f_entree:
            # Recherche des identifiants à 6 chiffres suivis d'un mot de passe
            match = re.search(r'https://account\.booking\.com/sign-in(?:/password)?[:|](\d{6})[:|]([^\s]+)', ligne)
            
            if match:
                identifiant, mot_de_passe = match.groups()
                f_sortie.write(f"{identifiant}:{mot_de_passe}\n")
    
    print(f"Extraction terminée. Résultats enregistrés dans {fichier_sortie}")

# Nom des fichiers (à adapter selon ton besoin)
fichier_source = "booking.txt"
fichier_resultat = "identifiants_mdp.txt"

# Exécuter l'extraction
extraire_identifiants(fichier_source, fichier_resultat)
