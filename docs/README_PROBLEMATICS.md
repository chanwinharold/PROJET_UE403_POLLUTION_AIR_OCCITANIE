# Problématiques

Pour ce projet, nous avons retenu 4 problématiques :

1.  Les communes bénéficiant de conditions climatiques favorables présentent-elles un niveau de vie médian plus élevé ?
2.  La qualité de l'air dans chaque type d'environnement, s'améliore ou se dégrade-t-elle au fil des années ?
3.  Existe-t-il une typologie d'environnement favorable à la vie socio-économique de la population ?
4.  Quels facteurs quantitatifs sont le plus impactés par le taux de concentration des polluants ?

Le challenge sera d'extraire les données sql nécessaires pour répondre à chacune des problématiques. Chaque fichier `.._query.sql` correspond à une problématique.

<u>Exemple :</u> <br> `01_query.sql` ==\> ***problématique 1*** <br> `02_query.sql` ==\> ***problématique 2*** <br> `...`

## Requêtes à effectuer

### Problématique 1 :

-   Récupérer les communes (`code_insee_com`, `nom_com`), leurs conditions climatiques (`R_med`, `NBJRR1_med`, `NBJRR5_med`, `NBJRR10_med`, `Tmin_med`, `Tmax_med`, `Tens_vap_med`, `Force_vent_med`, `Insolation_med`, `Rayonnement_med`) ainsi que la situation socio économique de la population (`niveau_vie_median_2021`) à l'aide de jointures.

### Problématique 2

-   Récupérer les champs (`jour`, `mois`, `annee`, `typologie`, `influence`, `nom_poll`, `valeur_poll`) de la table `UE403_MESURES_JOURNALIERE_POLLUTION` en regroupant les enregistrements par `typologie`.

### Problématique 3

-   Récupérer pour chaque type d'environnement (`typologie`, `influence`), la vie socio-économique de sa population (`niveau_vie_median_2021`, `nb_logements_2022`, `Pourcentage_appartements_2022`, `pourcentage_locataires_dans_résidence_principale_2022`, `evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage`, `population_municipale_2023`, `Taux_activite_tranche_15_64_en_2022`)

### Problématique 4

-   Analyse plus complète.

## Autres formulations

1.  Existe-t-il une relation statistiquement significative entre les variables climatiques (température, précipitations, ensoleillement, vent) et le niveau de vie médian des communes ?
2.  Observe-t-on une tendance significative à la hausse ou à la baisse des concentrations de NO2, PM10, O3 selon la typologie des stations entre X et Y ?
3.  Le type d’environnement (urbain, rural, périurbain) est-il associé à des différences significatives de niveau de vie médian et de taux d’activité ?
4.  Parmi les variables climatiques, géographiques et socio-économiques, lesquelles expliquent le mieux la variabilité des concentrations en polluants ?
