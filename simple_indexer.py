# === simple_indexer.py ===
# Ce module construit un index pour retrouver les fichiers contenant un mot donné.
# Il permet aussi de lister les lignes où le mot apparaît..
import re

from text_processor import clean_text, tokenize


def build_index(documents):
    """
    Construit un index {mot: {fichier: fréquence}} à partir d’un dictionnaire {nom_fichier: texte}.
    """
    index = {}
    for filename, text in documents.items():  # ✅ text est déjà le contenu, pas besoin de read_file
        cleaned = clean_text(text)
        words = tokenize(cleaned)
        for word in words:
            word = word.lower()
            if word not in index:
                index[word] = {}
            if filename not in index[word]:
                index[word][filename] = 0
            index[word][filename] += 1
    return index


def read_file(filepath):
    """Lit le contenu d'un fichier texte et retourne une chaîne de caractères.
    Gère les erreurs de lecture (fichier introuvable, encodage).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except OSError as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
        return ""


def search_word_in_index(word, index):
    """
    Recherche un mot dans l'index.
    Retourne les documents où il apparaît.
    """
    if word in index:
        return index[word]
    else:
        return []  # Le mot n'est pas trouvé dans l'index


def find_lines_with_word(word, text):
    """
    Retourne les lignes contenant exactement le mot donné (sensible aux mots complets).
    """
    lines_with_word = []
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.IGNORECASE)
    for line in text.split('\n'):
        if pattern.search(line):
            lines_with_word.append(line.strip())
    return lines_with_word
