# === simple_indexer.py ===
# Ce module construit un index pour retrouver les fichiers contenant un mot donné.
# Il permet aussi de lister les lignes où le mot apparaît.

def build_index(documents):
    """
    Construit un index simple : {mot: liste des documents où il apparaît}
    Paramètre : documents est un dict {nom_fichier: liste de mots}
    """
    
    pass

def search_word_in_index(word, index):
    """
    Recherche un mot dans l'index.
    Retourne les documents où il apparaît.
    """
    pass

def find_lines_with_word(word, text):
    """
    Recherche les lignes contenant le mot dans un texte.
    Utile pour afficher le contexte d’apparition.
    """
    pass
