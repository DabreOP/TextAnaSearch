# === text_processor.py ===
# Ce module contient les fonctions pour :
# - Charger des fichiers texte (un seul fichier ou un dossier entier)
# - Nettoyer le texte : convertir en minuscules, supprimer la ponctuation, etc.
# - Diviser le texte en mots (tokenisation)
# - Retourner une structure exploitable (liste de mots ou liste de documents)

import os
import re
def read_file(filepath):
    """
    Lit le contenu d'un fichier texte et retourne une chaîne de caractères.
    À faire : gérer les erreurs de lecture (fichier introuvable, encodage).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Erreur : le fichier {filepath} n'a pas été trouvé.")
        return ""
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
        return ""
    
    pass

def read_folder(folder_path):
    """
    Lit tous les fichiers texte dans un dossier.
    Retourne une liste de chaînes (chaque élément est un fichier).
    """
    if not os.path.isdir(folder_path):
        print(f"Erreur : {folder_path} n'est pas un dossier valide.")
        return []
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            content = read_file(filepath)
            if content:
                documents.append(content)
    return documents   
    pass   

def clean_text(text):
    """
    Nettoie le texte :
    - Met en minuscules
    - Supprime la ponctuation
    - Gère les caractères spéciaux (accents, symboles)
    Retourne une chaîne nettoyée.
    """
    text = text.lower()  # Convertir en minuscules
    text = re.sub(r'[^\w\s]', '', text)  # Supprimer la ponctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Supprimer les espaces multiples et les espaces en début/fin
    return text
    pass

def tokenize(text):
    """
    Découpe le texte nettoyé en mots (liste de mots).
    """
    words = text.split()  # Diviser le texte en mots
    return words
    pass
