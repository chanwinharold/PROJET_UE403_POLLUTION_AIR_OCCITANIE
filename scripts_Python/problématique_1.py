import csv
import sqlite3

def table_problematique_1():
    # Utiliser un context manager pour fermer automatiquement la connexion
    with sqlite3.connect(r"C:\Users\DELL\OneDrive\Bureau\COURS L2\SEMESTRE 2\PROJET_UE403_POLLUTION_AIR_OCCITANIE\bdd\UE403_DB.db") as conn:
        cursor = conn.cursor()

        # Jointure conservée si vous avez besoin de filtrer via M_J_P,
        # sinon remplacez par un simple SELECT sur UE403_SOCIO_ECONOMIQUES
        requete = """
            SELECT DISTINCT
                typologie,
                influence,
                niveau_vie_median_2021                                          AS niveau_vie_median,
                nb_logements_2022                                               AS total_logements,
                pourcentage_appartements_2022                                   AS moy_pourcentage_appartements,
                pourcentage_locataires_dans_résidence_principale_2022           AS moy_locataires,
                evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage AS evolution_population,
                population_municipale_2023                                      AS population_totale,
                taux_activite_tranche_15_64_en_2022                             AS taux_activite
            FROM UE403_MESURES_JOURNALIERE_POLLUTION AS M_J_P
            INNER JOIN UE403_SOCIO_ECONOMIQUES AS S_E ON S_E.code_insee_com = M_J_P.code_insee_com;
        """

        cursor.execute(requete)
        res = cursor.fetchall()

        print("Résultats de la requête :")
        for ligne in res:
            print(ligne)


        with open("resultat.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'typologie',
                'influence',
                'niveau_vie_median_2021',
                'nb_logements_2022',
                'pourcentage_appartements_2022',
                'pourcentage_locataires_dans_residence_principale_2022',
                'evolution_population_2017_2023',
                'population_municipale_2023',
                'taux_activite_15_64_2022'
            ])
            writer.writerows(res)

        print(f"{len(res)} lignes écrites dans resultat.csv")

table_problematique_1()
