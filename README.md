# PROJET_UE403_POLLUTION_AIR_OCCITANIE

```
PROJET_UE403_POLLUTION_AIR_OCCITANIE/
│
├── 📁 donnees/
│   ├── brutes/
│   │   ├── qualite_air_occitanie.csv
│   │   ├── donnees_geo_climatiques.csv
│   │   ├── donnees_socio_economiques.csv
│   │   └── descriptif_donnees.html
│   │
│   ├── traitees/
│   │   ├── tables_extraites/
│   │   │   ├── table_polluants.csv
│   │   │   ├── table_communes.csv
│   │   │   └── autres_extractions.csv
│   │   └── donnees_complementaires/
│   │       └── (éventuelles données web)
│   │
│   └── README_donnees.txt (description des fichiers)
│
├── 📁 bdd/
│   ├── scripts_creation/
│   │   ├── 01_creation_bdd.sql
│   │   ├── 02_import_donnees.sql
│   │   └── 03_contraintes_index.sql
│   │
│   ├── requetes/
│   │   ├── requetes_extraction.sql
│   │   └── requetes_analyses.sql
│   │
│   └── schema_bdd.pdf (schéma entité-association)
│
├── 📁 scripts_R/
│   ├── 00_chargement_packages.R
│   ├── 01_import_nettoyage.R
│   ├── 02_statistiques_univariees.R
│   ├── 03_statistiques_bivariees.R
│   ├── 04_graphiques.R
│   └── 05_analyses_problematiques.R
│
├── 📁 analyses/
│   ├── univariee/
│   │   ├── graphiques/
│   │   └── resultats/
│   │
│   ├── bivariee/
│   │   ├── graphiques/
│   │   └── resultats/
│   │
│   └── problematiques/
│       ├── problematique_1/
│       ├── problematique_2/
│       └── ... (jusqu'à 5 max)
│
├── 📁 rapport/
│   ├── rapport_final.Rmd
│   ├── rapport_final.pdf (généré)
│   ├── bibliographie.bib (si nécessaire)
│   └── images/
│       └── (logos, images pour le rapport)
│
├── 📁 presentation_orale/
│   ├── presentation_seance7.pptx
│   ├── diagramme_gantt.pptx (ou intégré dans présentation)
│   └── notes_presentation.txt
│
├── 📁 organisation/
│   ├── planning_gantt.xlsx
│   ├── repartition_taches.txt
│   ├── compte_rendus_seances/
│   │   ├── CR_seance_01.txt
│   │   ├── CR_seance_02.txt
│   │   └── ...
│   └── participation_membres.txt
│
├── 📁 documents_reference/
│   ├── consignes_projet.pdf
│   ├── tutoriels/
│   └── ressources_IRIS/
│
└── README.md (description générale du projet)
```