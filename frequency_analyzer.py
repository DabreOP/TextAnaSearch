"""Fonction pour calculer la fréquence de chaque mot dans un texte
ou un ensemble de textes (utilisation de dictionnaires).
Fonction pour trier les mots par fréquence (décroissante) pour
identiﬁer les plus communs.
A ichage des N mots les plus fréquents.
Auto-apprentissage : Utilisation e icace des dictionnaires
(collections.Counter s'ils le découvrent), tri de dictionnaires par
valeur."""
from collections import Counter
def calculate_word_frequency(texts):
    """
    Calculate the frequency of each word in a list of texts.

    Args:
        texts (list of str): List of strings where each string is a text.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    word_count = Counter()
    
    for text in texts:
        words = text.split()
        word_count.update(words)
    
    return dict(word_count)
def sort_words_by_frequency(word_freq):
    """Sort words by their frequency in descending order.
    