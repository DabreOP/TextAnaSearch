# === frequency_analyzer.py ===
# Ce module calcule la fréquence des mots dans un texte ou une liste de documents.
# Il permet aussi d’afficher les mots les plus fréquents.

from collections import Counter

def compute_frequencies(words):
    """
    Prend une liste de mots, retourne un dictionnaire {mot: fréquence}
    Utilise collections.Counter pour simplifier.
    """
    if not isinstance(words, list):
        raise ValueError("Les mots doivent être fournis sous forme de liste.")
    return Counter(words)
    pass

def top_n_words(freq_dict, n=10):
    """
    Trie les mots par fréquence décroissante.
    Retourne une liste des N mots les plus fréquents.
    """
    if not isinstance(freq_dict, dict):
        raise ValueError("Le dictionnaire de fréquences doit être fourni.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N doit être un entier positif.")
    return freq_dict.most_common(n)
    pass

def display_top_words(top_words):
    """
    Affiche les mots les plus fréquents avec leur fréquence.
    """
    if not isinstance(top_words, list):
        raise ValueError("Les mots les plus fréquents doivent être fournis sous forme de liste.")
    for word, freq in top_words:
        print(f"{word}: {freq} fois")
        return None
    pass
