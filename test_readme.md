# 📈 FinanceLake

**FinanceLake** est un projet open-source dédié à l’ingestion et à l’analyse de données financières, en particulier des données boursières issues de Yahoo Finance via la bibliothèque `yfinance`.

Ce dépôt comprend une fonction clé (`fetch_stock_data`) et son jeu de tests unitaires permettant de garantir sa fiabilité et son bon fonctionnement.

---

## 🎯 Objectifs

- Récupérer les données boursières à partir de Yahoo Finance.
- Retourner les colonnes essentielles : `Open`, `Close`, `Volume`.
- Assurer la fiabilité de la fonction à l’aide de tests unitaires.
- Éviter les appels réels à l'API dans les pipelines CI/CD en utilisant du mocking.

---

## 🗂️ Structure du projet

financelake/
├── stock_ingestion.py # Contient la fonction fetch_stock_data
├── tests/
│ └── test_stock_ingestion.py # Tests unitaires (réels et mockés)
├── requirements.txt # Liste des dépendances
└── README.md # Ce fichier

## 🧪 Tests unitaires

Le projet utilise `pytest` pour valider le bon fonctionnement de la fonction `fetch_stock_data`.

### ✔️ Ce que les tests vérifient

- La fonction retourne un `DataFrame` non vide.
- Les colonnes `Open`, `Close` et `Volume` sont bien présentes.
- Les appels à `yfinance.Ticker().history()` sont mockés lors des tests CI/CD.

## 📌 Exécution des tests

```bash
pytest

##  Assurez-vous d’avoir installé les dépendances ci-dessous.

1. Cloner le dépôt :

git clone https://github.com/votre-utilisateur/financelake.git
cd financelake

2. Créer et activer un environnement virtuel :

python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows


3. Installer les dépendances :

pip install -r requirements.txt

👨‍💻 Contribution

Les contributions sont les bienvenues !

Forkez ce dépôt.

Créez une branche : git checkout -b nouvelle-fonctionnalite.

Commitez vos modifications : git commit -m "Ajout d’une fonctionnalité".

Pushez sur votre fork : git push origin nouvelle-fonctionnalite.

Créez une Pull Request.