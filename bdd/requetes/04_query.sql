SELECT
    code_insee_com,
    nom_poll,
    ROUND(MEDIAN(valeur_poll), 2) AS valeur_poll_med,
    ROUND(AVG(valeur_poll), 2) AS valeur_poll_avg,
    niveau_vie_median_2021,
    nb_logements_2022,
    Pourcentage_appartements_2022,
    pourcentage_locataires_dans_résidence_principale_2022,
    evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage,
    population_municipale_2023,
    Taux_activite_tranche_15_64_en_2022,
    population, superficie_km2, densite,
    alti_med, RR_med, NBJRR1_med, NBJRR5_med, NBJRR10_med,
    Tmin_med, Tmax_med, Tens_vap_med, Force_vent_med, Insolation_med, Rayonnement_med
FROM UE403_SOCIO_ECONOMIQUES SE
         INNER JOIN UE403_GEO_CLIMATIQUES GC USING (code_insee_com)
         INNER JOIN UE403_MESURES_JOURNALIERE_POLLUTION USING (code_insee_com)
GROUP BY code_insee_com;

SELECT *
FROM (
         SELECT
             code_insee_com,
             nom_poll,
             ROUND(MEDIAN(valeur_poll), 2) AS valeur_poll_med,
             ROUND(AVG(valeur_poll), 2) AS valeur_poll_avg,
             niveau_vie_median_2021,
             nb_logements_2022,
             Pourcentage_appartements_2022,
             pourcentage_locataires_dans_résidence_principale_2022,
             evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage,
             population_municipale_2023,
             Taux_activite_tranche_15_64_en_2022,
             population, superficie_km2, densite,
             alti_med, RR_med, NBJRR1_med, NBJRR5_med, NBJRR10_med,
             Tmin_med, Tmax_med, Tens_vap_med, Force_vent_med, Insolation_med, Rayonnement_med
         FROM UE403_SOCIO_ECONOMIQUES SE
                  INNER JOIN UE403_GEO_CLIMATIQUES GC USING (code_insee_com)
                  INNER JOIN UE403_MESURES_JOURNALIERE_POLLUTION USING (code_insee_com)
         GROUP BY code_insee_com
) t
LIMIT 0;