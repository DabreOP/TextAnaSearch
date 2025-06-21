"""
text_processor.py

Ce module contient les fonctions pour :
- Charger des fichiers texte (un seul fichier ou un dossier entier)
- Nettoyer le texte : convertir en minuscules, supprimer la ponctuation, etc.
- Diviser le texte en mots (tokenisation)
- Retourner une structure exploitable (liste de mots ou liste de documents).
"""

# text_processor.py
import os
import re


def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Erreur de lecture du fichier {filepath} : {e}")
        return ""


def read_folder(folder_path, return_filenames=False):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if return_filenames:
                        documents.append((path, content))  # ✅ retourne le chemin réel.
                    else:
                        documents.append(content)
            except Exception as e:
                print(f"Erreur de lecture du fichier {filename} : {e}")
    return documents


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return text


def tokenize(text):
    return text.split()

