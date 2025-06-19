# cli_manager.py---


from text_processor import read_file, clean_text, tokenize
from frequency_analyzer import compute_frequencies, top_n_words, display_top_words
from simple_indexer import build_index, search_word_in_index, find_lines_with_word
from document_retriever import retrieve_documents, sort_by_relevance
from tkinter import Tk, filedialog
import os

documents = {}  # nom de fichier réel -> texte nettoyé


def show_menu():
    
    print("=== Menu Principal ===")
    print("1. Charger des fichiers")
    print("2. Analyse de fréquence")
    print("3. Rechercher un mot")
    print("4. Rechercher par mots-clés")
    print("5. Quitter")


def get_txt_files_or_dirs():
    root = Tk()
    root.withdraw()

    print("\nSouhaitez-vous charger :")
    print("1. Un ou plusieurs fichiers .txt")
    print("2. Un dossier contenant des fichiers .txt")
    choix = input("Votre choix (1-2) : ")

    if choix == '1':
        files = filedialog.askopenfilenames(
            title="Sélectionner des fichiers texte",
            filetypes=[("Fichiers texte", "*.txt")]
        )
        return list(files)

    elif choix == '2':
        folder = filedialog.askdirectory(
            title="Sélectionner un dossier contenant des fichiers texte"
        )
        if folder:
            txt_files = []
            for filename in os.listdir(folder):
                if filename.endswith('.txt'):
                    txt_files.append(os.path.join(folder, filename))
            return txt_files
        else:
            return []

    else:
        print("Choix invalide.")
        return []


def get_user_choice():
    global documents

    choice = input("Entrez votre choix (1-5) : ")

    if choice == '1':
        file_paths = get_txt_files_or_dirs()
        if not file_paths:
            print("Aucun fichier sélectionné.")
            return

        documents.clear()
        for path in file_paths:
            filename = os.path.basename(path)
            content = read_file(path)
            cleaned = clean_text(content)
            documents[filename] = cleaned

        print(f"{len(documents)} fichiers chargés avec succès :")
        for name in documents.keys():
            print(f" - {name}")

    elif choice == '2':
        if not documents:
            print("Veuillez d'abord charger des fichiers (option 1).")
            return

        for filename, text in documents.items():
            words = tokenize(text)
            frequencies = compute_frequencies(words)
            top_words = top_n_words(frequencies, 10)

            print(f"\nFichier : {filename}")
            display_top_words(top_words)
            print(f"Analyse de fréquence pour {len(words)} mots.")

    elif choice == '3':
        word = input("Entrez le mot à rechercher : ").lower()
        index = build_index(documents)

        if word in index:
            results = search_word_in_index(word, index)
            print(f"\nLe mot '{word}' a été trouvé dans les documents suivants :")
            for doc in results:
                print(f"\nFichier : {doc}")
                text = documents[doc]
                lines = find_lines_with_word(word, text)
                for line in lines:
                    print(f"  - {line}")
        else:
            print(f"\nLe mot '{word}' n'a été trouvé dans aucun document.")

    elif choice == '4':
        query = input("Entrez les mots-clés à rechercher (séparés par des espaces) : ")
        query_words = query.lower().split()
        index = build_index(documents)

        results = retrieve_documents(query_words, index, documents)
        if results:
            sorted_results = sort_by_relevance(results)
            print("Documents trouvés par mots-clés :")
            for doc, score in sorted_results:
                print(f"\n{doc} (score: {score})")

                text = documents[doc]
                words_in_doc = []
                for word in query_words:
                    matching_words = [w for w in index if w.startswith(word)]
                    words_in_doc.extend(matching_words)

                words_in_doc = list(set(words_in_doc))

                for word in words_in_doc:
                    lines = find_lines_with_word(word, text)
                    if lines:
                        print(f"\nMots commençant par '{word}':")
                        for line in lines:
                            print(f"  - {line}")
        else:
            print("Aucun document trouvé avec les mots-clés donnés.")

    elif choice == '5':
        print("Au revoir !")
        exit(0)

    else:
        print("Choix invalide, veuillez réessayer.")


def run():
    while True:
        show_menu()
        get_user_choice()
