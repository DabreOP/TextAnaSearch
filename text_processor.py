"""
Fonctions pour lire le contenu de ﬁchiers texte (individuels ou d'un
dossier).o
o
o
Fonctions pour nettoyer le texte : convertir en minuscules,
supprimer la ponctuation spéciﬁque, diviser le texte en mots
(tokenisation).
Gestion d'une collection de documents (ex : liste de chaînes, ou
liste de listes de mots).
Auto-apprentissage : Expressions régulières (basiques) pour le
nettoyage avancé, gestion des encodages de ﬁchiers."""
import os
import re
from collections import Counter

def lire_fichiers_dossier(dossier):
    """
    Lit tous les fichiers texte dans un dossier et retourne leur contenu.
    
    :param dossier: str, le chemin du dossier contenant les fichiers texte.
    :return: list, une liste de chaînes contenant le contenu de chaque fichier.
    """
    textes = []
    for nom_fichier in os.listdir(dossier):
        if nom_fichier.endswith('.txt'):
            with open(os.path.join(dossier, nom_fichier), 'r', encoding='utf-8') as f:
                textes.append(f.read())
    return textes

def nettoyer_texte(texte): 
    """
    Nettoie le texte en le convertissant en minuscules, en supprimant la ponctuation et en tokenisant les mots.
    
    :param texte: str, le texte à nettoyer.
    :return: list, une liste de mots nettoyés.
    """
    # Convertir en minuscules
    texte = texte.lower()
    
    # Supprimer la ponctuation spécifique (ici on enlève tout sauf les lettres et les espaces)
    texte = re.sub(r'[^\w\s]', '', texte)
    
    # Tokenisation : diviser le texte en mots
    mots = texte.split()
    
    return mots
def traiter_textes(textes):
    """
    Traite une liste de textes en nettoyant et en comptant la fréquence des mots.
    """
    """
    :param textes: list, une liste de chaînes contenant les textes à traiter.
    :return: Counter, un dictionnaire avec les mots comme clés et leurs fréquences comme valeurs.
    """
    mots_nettoyes = []
    for texte in textes:
        mots_nettoyes.extend(nettoyer_texte(texte))
    
    return Counter(mots_nettoyes)
def afficher_mots_frequents(frequences, n=10):
    """
    Affiche les N mots les plus fréquents."""
    mots_frequents = frequences.most_common(n)
    for mot, freq in mots_frequents:
        print(f"{mot}: {freq}")
        
def analyser_dossier(dossier, n=10):
    