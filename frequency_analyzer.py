"""Fonction pour calculer la fréquence de chaque mot dans un texte 
ou un ensemble de textes  (utilisation de dictionnaires).
Fonction pour trier les mots par fréquence (décroissante) pour
identiﬁer les plus communs.
A ichage des N mots les plus fréquents.
Auto-apprentissage : Utilisation e icace des dictionnaires
(collections.Counter s'ils le découvrent), tri de dictionnaires par
valeur. 
valable aussi pour les fichiers txt"""
from collections import Counter

def calcul_mot_frequence(texts):
    """
    Calcule la fréquence de chaque mot dans un texte ou un ensemble de textes.
    
    :param texts: str ou liste de str, le texte ou les textes à analyser.
    :return: Counter, un dictionnaire avec les mots comme clés et leurs fréquences comme valeurs.
    """
    if isinstance(texts, str):
        texts = [texts]
    
    # Joindre tous les textes en une seule chaîne
    all_text = ' '.join(texts)
    
    # Séparer les mots et compter leur fréquence
    mots = all_text.split()
    return Counter(mots)

def trier_mots_par_frequence(frequences):
    """
    Trie les mots par fréquence décroissante.
    
    :param frequences: Counter, un dictionnaire avec les mots et leurs fréquences.
    :return: list, une liste de tuples (mot, fréquence) triée par fréquence décroissante.
    """
    return frequences.most_common()

def afficher_mots_frequents(frequences, n=10):
    """
    Affiche les N mots les plus fréquents.
    
    :param frequences: Counter, un dictionnaire avec les mots et leurs fréquences.
    :param n: int, le nombre de mots à afficher (par défaut 10).
    """
    mots_frequents = trier_mots_par_frequence(frequences)
    for mot, freq in mots_frequents[:n]:
        print(f"{mot}: {freq}")
        
# Exemple d'utilisation avec un fichier worldlist.txt
def analyser_fichier(fichier, n=10):
    """
    Analyse un fichier texte pour afficher les N mots les plus fréquents.
    
    :param fichier: str, le chemin du fichier à analyser.
    :param n: int, le nombre de mots à afficher (par défaut 10).
    """

    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            texte = f.read()
        frequences = calcul_mot_frequence(texte)
        afficher_mots_frequents(frequences, n)
    except FileNotFoundError:
        print(f"Fichier non trouvé: {fichier}")
    
    # Exemple d'utilisation
    texte_exemple = "Bonjour le monde. Bonjour à tous. Le monde est beau."
    frequences = calcul_mot_frequence(texte_exemple)
    afficher_mots_frequents(frequences, 5)
    
    # Analyser un fichier texte
    analyser_fichier('requirement.txt', 10)
