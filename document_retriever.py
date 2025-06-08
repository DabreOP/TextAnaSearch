# === document_retriever.py ===
# Ce module recherche les documents contenant certains mots-clés
# et les classe par pertinence.

def retrieve_documents(query_words, index, documents):
    """
    Retourne la liste des documents contenant au moins un mot-clé.
    Classement basé sur le nombre de mots-clés présents.
    """
    results = []
    for word in query_words:
        if word in index:
            for doc in index[word]:
                if doc not in results:
                    results.append(doc)
    # Calculer la pertinence pour chaque document
    results_with_relevance = [(doc, compute_relevance(documents[doc], query_words)) for doc in results]
    # Trier les résultats par pertinence
    sorted_results = sort_by_relevance(results_with_relevance)
    return sorted_results
    # Retourne une liste de tuples (document, score de pertinence)
    pass

def compute_relevance(doc, query_words):
    """
    Calcule un score de pertinence pour un document donné.
    Ex : nombre de mots-clés présents dans le document.
    """
    words = doc.split()  # Tokenisation simple
    score = sum(1 for word in query_words if word in words)
    return score
    # Retourne un score de pertinence basé sur les mots-clés présents
    pass

def sort_by_relevance(results):
    """
    Trie les documents selon leur score de pertinence.
    """
    return sorted(results, key=lambda x: x[1], reverse=True)
    # Retourne une liste triée de tuples (document, score de pertinence)
    pass
