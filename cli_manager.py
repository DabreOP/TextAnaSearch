# === cli_manager.py ===
# Ce fichier fournit l’interface principale de l’application.
# Il propose un menu pour charger les fichiers, lancer une analyse,
# faire des recherches, afficher les résultats, sauvegarder.

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
    pass

def run():
    """
    Fonction principale qui boucle sur le menu.
    """
    pass
