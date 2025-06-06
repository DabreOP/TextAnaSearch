# === text_processor.py ===
# Ce module contient les fonctions pour :
# - Charger des fichiers texte (un seul fichier ou un dossier entier)
# - Nettoyer le texte : convertir en minuscules, supprimer la ponctuation, etc.
# - Diviser le texte en mots (tokenisation)
# - Retourner une structure exploitable (liste de mots ou liste de documents)

import os
import re


def read_file(filepath):
    """Lit le contenu d'un fichier texte et retourne une chaîne de caractères.
    À faire : gérer les erreurs de lecture (fichier introuvable, encodage)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filepath} n'a pas été trouvé.")
        return ""
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
        return ""

def read_folder(folder_path):
    """
    Lit tous les fichiers texte dans un dossier.
    Retourne une liste de chaînes (chaque élément est un fichier).
    """
    documents = []
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                filepath = os.path.join(folder_path, filename)
                content = read_file(filepath)
                if content:  # Ajouter seulement si le contenu n'est pas vide
                    documents.append(content)
    except FileNotFoundError:
        print(f"Erreur : Le dossier {folder_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du dossier {folder_path} : {e}")
    return documents

def clean_text(text):
    """Nettoie le texte : convertit en minuscules, supprime la ponctuation et les chiffres."""
    text = text.lower()  # Convertir en minuscules
    text = re.sub(r'[^\w\s]', '', text)  # Supprimer la ponctuation
    text = re.sub(r'\d+', '', text)  # Supprimer les chiffres
    return text

def tokenize_text(text):
    """Divise le texte en mots (tokenisation) et retourne une liste de mots."""
    text = clean_text(text)  # Nettoyer le texte avant la tokenisation
    return text.split()  # Diviser par les espaces pour obtenir les mots
def process_text(filepath_or_folder):
    """Charge et traite le texte d'un fichier ou d'un dossier.
    Retourne une liste de mots ou une liste de documents."""
    if os.path.isdir(filepath_or_folder):
        # Si c'est un dossier, lire tous les fichiers texte
        documents = read_folder(filepath_or_folder)
        return [tokenize_text(doc) for doc in documents]  # Liste de listes de mots
    elif os.path.isfile(filepath_or_folder):
        # Si c'est un fichier, lire le contenu et le tokeniser
        content = read_file(filepath_or_folder)
        return tokenize_text(content)  # Liste de mots
    else:
        print(f"Erreur : {filepath_or_folder} n'est ni un fichier ni un dossier.")
        return []
    
# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez 'votre_fichier.txt' ou 'votre_dossier' par le chemin réel
    result = process_text('requirements.txt')
    print(result)  # Affiche la liste de mots du fichier
    # Pour un dossier, utilisez process_text('votre_dossier'