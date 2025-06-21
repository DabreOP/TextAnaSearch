# 📁 TextAnaSearch

TextAnaSearch est un moteur de recherche de texte simple en ligne de commande, écrit en Python.  
Il permet d’analyser un ou plusieurs fichiers `.txt` pour compter la fréquence des mots, rechercher des mots-clés et afficher les documents les plus pertinents.

---

## 👥 Membres du Projet

- **DABREO PEREIRA** – Responsable du projet, structure générale, création de `main.py`, encadrement Git/GitHub.
- **Membre 1*BINTI MWESA Sarah* – Développement de `text_processor.py` (lecture et nettoyage des fichiers).
- **Membre 2*DABREO PEREIRA Victor* – Développement de `frequency_analyzer.py` (analyse de fréquence).
- **Membre 3*BUKASA MULAJI Jael* – Développement de `simple_indexer.py` (indexation et recherche de mots).
- **Membre 4*BUNIBWABO MUBENGA Merveille* – Développement de `document_retriever.py` (recherche par mots-clés et classement).
- **Membre 5*DABREO PEREIRA Victor* – Développement de `cli_manager.py` (interface utilisateur et menu principal).

---

## 🧠 Fonctionnalités

- Charger un ou plusieurs fichiers `.txt`.
- Nettoyer le texte (ponctuation, majuscules...).
- Compter la fréquence des mots (analyse statistique).
- Rechercher un mot et afficher les lignes concernées.
- Rechercher par mots-clés (avec classement par pertinence).
- Interface CLI + sélection de fichiers avec `tkinter`.

---

## 🛠️ Installation

```bash
git clone https://github.com/DabreOP/TextAnaSearch.git
cd TextAnaSearch
python3 -m venv venv
source venv/bin/activate  # Sous Linux
pip install -r requirements.txt  # (si vous ajoutez un fichier requirements)
