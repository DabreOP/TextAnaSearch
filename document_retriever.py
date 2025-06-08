# === document_retriever.py ===
# Ce module recherche les documents contenant certains mots-clés
# et les classe par pertinence.

def retrieve_documents(query_words, index, documents):
    """
    Retourne un dictionnaire {nom_fichier: score} des documents contenant des mots
    correspondant à chaque mot-clé ou à un mot commençant par ce mot-clé.
    """
    results = {}

    for word in query_words:
        word = word.lower()
        for indexed_word in index:
            if indexed_word.startswith(word):  # correspond à des mots comme "pycodestyle"
                for filename in index[indexed_word]:
                    results[filename] = results.get(filename, 0) + 1

    return results


def compute_relevance(doc_text, query_words):
    """
    Calcule un score de pertinence pour un document donné.
    Ex : nombre de mots-clés présents dans le texte du document.
    """
    words = doc_text.lower().split()  # Tokenisation simple
    score = sum(1 for word in query_words if word.lower() in words)
    return score


def sort_by_relevance(results):
    """
    Trie les résultats en fonction du score de pertinence.
    """
    return sorted(results.items(), key=lambda x: x[1], reverse=True)


def find_lines_with_word(word, text):
    """
    Retourne les lignes du texte qui contiennent le mot spécifié.
    """
    lines_with_word = []
    for line in text.splitlines():
        if word.lower() in line.lower():
            lines_with_word.append(line.strip())
    return lines_with_word
