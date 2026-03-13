SELECT 
    typologie,
    influence,
    niveau_vie_median_2021 AS niveau_vie_median,
    nb_logements_2022 AS total_logements,
    pourcentage_appartements_2022 AS moy_pourcentage_appartements,
    pourcentage_locataires_dans_résidence_principale_2022 AS moy_locataires,
    evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage AS evolution_population,
    population_municipale_2023 AS population_totale,
    taux_activite_tranche_15_64_en_2022 AS taux_activite
FROM UE403_MESURES_JOURNALIERE_POLLUTION AS M_J_P 
INNER JOIN UE403_SOCIO_ECONOMIQUES AS S_E ON S_E.code_insee_com = M_J_P.code_insee_com;