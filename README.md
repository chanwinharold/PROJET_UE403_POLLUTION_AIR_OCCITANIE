# PROJET_UE403_POLLUTION_AIR_OCCITANIE

Ce projet porte sur l'analyse de la pollution de l'air en Occitanie, intégrant des données géoclimatiques et socio-économiques.

## Structure du Projet

```
PROJET_UE403_POLLUTION_AIR_OCCITANIE/
│
├── 📁 donnees/
│   ├── brutes/
│   │   ├── donnees_geo_climatiques.csv
│   │   ├── donnees_socio_economiques.csv
│   │   └── mesures_occitanie_journaliere_pollution.csv
│   ├── traitees/
│   ├── README_descritpion_des_données.md
│   └── notebook.ipynb
│
├── 📁 bdd/
│   ├── scripts_creation/
│   │   ├── database.py       (Classe de gestion SQLite)
│   │   └── main.py           (Script de création et import)
│   ├── requetes/
│   └── UE403_DB.db           (Base de données SQLite)
│
├── 📁 scripts_Python/
│   └── extraction.py         (Utilitaire de lecture CSV)
│
├── 📁 scripts_R/             (Analyses statistiques)
│
├── requirements.txt          (Dépendances Python)
├── LICENSE
└── README.md
```

## Installation

1. Cloner le dépôt.
2. Installer les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Base de données
Pour initialiser la base de données SQLite et importer les données brutes :
```bash
cd bdd/scripts_creation
python main.py
```
Cela créera le fichier `bdd/UE403_DB.db` avec les tables correspondantes aux fichiers CSV.

### Analyses
- Le dossier `scripts_R/` contient les scripts pour les statistiques univariées, bivariées et les graphiques.
- `donnees/notebook.ipynb` peut être utilisé pour des explorations de données.