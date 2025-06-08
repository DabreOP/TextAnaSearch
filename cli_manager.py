# === cli_manager.py ===
# Ce fichier fournit l’interface principale de l’application.
# Il propose un menu pour charger les fichiers, lancer une analyse,
# faire des recherches, afficher les résultats, sauvegarder.

from text_processor import read_file, read_folder, clean_text, tokenize
from frequency_analyzer import compute_frequencies, top_n_words, display_top_words
from simple_indexer import build_index, search_word_in_index, find_lines_with_word
from document_retriever import retrieve_documents, sort_by_relevance
# Importation des modules nécessaires pour le gestionnaire de ligne de commande

def show_menu():
    """
    Affiche les options du menu utilisateur :
    1. Charger des fichiers
    2. Analyse de fréquence
    3. Rechercher un mot
    4. Rechercher par mots-clés
    5. Quitter
    """
    print("=== Menu Principal ===")
    print("1. Charger des fichiers")
    print("2. Analyse de fréquence")
    print("3. Rechercher un mot")
    print("4. Rechercher par mots-clés")
    print("5. Quitter")
    
    pass

def get_user_choice():
    """
    Récupère le choix de l'utilisateur et redirige vers les fonctions correspondantes.
    """
    choice = input("Entrez votre choix (1-5) : ")
    if choice == '1':
        # Appeler la fonction pour charger des fichiers
        pass
    elif choice == '2':
        # Appeler la fonction pour l'analyse de fréquence
        pass
    elif choice == '3':
        # Appeler la fonction pour rechercher un mot
        pass
    elif choice == '4':
        # Appeler la fonction pour rechercher par mots-clés
        pass
    elif choice == '5':
        print("Au revoir !")
        exit(0)
    else:
        print("Choix invalide, veuillez réessayer.")
        get_user_choice()
        # Redemander le choix à l'utilisateur  
    pass

def run():
    """
    Fonction principale qui boucle sur le menu.
    """
    while True:
        show_menu()
        get_user_choice()
        # Boucle pour afficher le menu et traiter les choix de l'utilisateur
        # Vous pouvez ajouter ici des appels aux autres modules pour charger les fichiers,
        # effectuer des analyses, etc. 
        # Pour l'instant, on ne fait rien de plus. 
    pass
