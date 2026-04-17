# CHANWIN Harold


from modules.database import DBCreation
from modules.extraction import DataManager

###################################################################
########### FONCTION DE CRÉATION DE LA BD ET DES TABLES ###########
###################################################################

FILE_PATHS = {
    0 : "./donnees/brutes/donnees_geo_climatiques.csv",
    1 : "./donnees/brutes/donnees_socio_economiques.csv",
    2 : "./donnees/brutes/mesures_occitanie_journaliere_pollution.csv"
}
TABLE_NAMES = {
    0 : "UE403_Geo_climatiques_provisoire",
    1 : "UE403_Socio_economiques_provisoire",
    2 : "UE403_Mesures_occitanie_journaliere_pollution_provisoire"
}

def creation():
    """
    Cette fonction permet de créer la base de données et
    les différentes tables issues des fichiers à notre disposition
    """
    db = DBCreation(DATABASE_PATH)

    for i in range(len(FILE_PATHS)):
        db.drop_table(table_name_=TABLE_NAMES[i])
        db.create_table(filepath_=FILE_PATHS[i], table_name_=TABLE_NAMES[i])
        db.insert_values(filepath_=FILE_PATHS[i], table_name_=TABLE_NAMES[i])

    db.drop_table("UE403_COMMUNES")
    db.drop_table("UE403_DEPARTEMENTS")
    db.drop_table("UE403_STATIONS")
    db.drop_table("UE403_LIEN_COMMU_DEPT")
    db.drop_table("UE403_GEO_CLIMATIQUES")
    db.drop_table("UE403_MESURES_JOURNALIERE_POLLUTION")
    db.drop_table("UE403_SOCIO_ECONOMIQUES")

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_COMMUNES AS
            SELECT code_insee_com, nom_com
            FROM UE403_Geo_climatiques_provisoire
            WHERE reg_code = 76 AND reg_nom = 'Occitanie'
            GROUP BY code_insee_com, nom_com;
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_DEPARTEMENTS AS
            SELECT dep_code, dep_nom
            FROM UE403_Geo_climatiques_provisoire
            WHERE reg_code = 76 AND reg_nom = 'Occitanie'
            GROUP BY dep_code, dep_nom;
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_STATIONS AS
            SELECT code_station, nom_station
            FROM UE403_Mesures_occitanie_journaliere_pollution_provisoire
            GROUP BY code_station, nom_station;
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_LIEN_COMMU_DEPT AS
            SELECT code_insee_com, dep_code
            FROM UE403_Geo_climatiques_provisoire
            WHERE reg_code = 76 AND reg_nom = 'Occitanie'
            GROUP BY code_insee_com, dep_code;
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_GEO_CLIMATIQUES AS
            SELECT population, superficie_km2, densite, latitude, longitude, densite_cat, alti_med, RR_med, NBJRR1_med, NBJRR5_med, NBJRR10_med, Tmin_med, Tmax_med, Tens_vap_med, Force_vent_med, Insolation_med, Rayonnement_med, code_insee_com
            FROM UE403_Geo_climatiques_provisoire
            WHERE reg_code = 76 AND reg_nom = 'Occitanie';
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_SOCIO_ECONOMIQUES AS
            SELECT niveau_vie_median_2021, nb_logements_2022, Pourcentage_appartements_2022, pourcentage_locataires_dans_résidence_principale_2022, evolution_annuelle_moy_de_la_population_entre_2017_et_2023_en_pourcentage, population_municipale_2023, Taux_activite_tranche_15_64_en_2022, code_insee_com
            FROM UE403_Socio_economiques_provisoire;
    """)

    db.execute_query("""
        CREATE TABLE IF NOT EXISTS UE403_MESURES_JOURNALIERE_POLLUTION AS
            SELECT jour, mois, annee, typologie, influence, nom_poll, valeur_poll, code_insee_com, code_station
            FROM UE403_Mesures_occitanie_journaliere_pollution_provisoire;
    """)

    for i in range(len(FILE_PATHS)):
        db.drop_table(TABLE_NAMES[i])

    print("CREATION DONE ✅ 🎉")



###################################################################
############### FONCTION CRÉATION DES FICHIERS CSV ################
###################################################################

DATABASE_PATH = "./bdd/UE403_DB.db"

FILENAMES = [
    "problematic_01.csv",
    "problematic_02.csv",
    "problematic_03.csv",
    "problematic_04.csv"
]
QUERIES = {
    0 : """
        SELECT  c.code_insee_com, c.nom_com, cl.RR_med,NBJRR5_med,cl.NBJRR1_med,cl.NBJRR10_med,cl.Tmin_med,cl.Tmax_med,cl.Tens_vap_med,cl.Force_vent_med,
                cl.Insolation_med,cl.Rayonnement_med,se.niveau_vie_median_2021
        FROM UE403_COMMUNES  c
                 JOIN UE403_GEO_CLIMATIQUES  cl
                      ON c.code_insee_com = cl.code_insee_com
                 JOIN UE403_SOCIO_ECONOMIQUES  se
                      ON c.code_insee_com = se.code_insee_com;
        """,
    1 : """
        select jour, mois, annee, typologie, influence, nom_poll, valeur_poll
        from "UE403_MESURES_JOURNALIERE_POLLUTION"
        order by typologie;
        """,
    2 : """
        SELECT DISTINCT
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
        """,
    3 : """
        SELECT
            code_insee_com, nom_poll,
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
        """
}

def transformation():
    """
    Cette fonction transforme les tables issues de nos requêtes en fichier csv
    exploitables par nos fichiers R pour l'analyse de données.
    """
    dm = DataManager()
    for i in range(len(QUERIES)):
        dm.write(
            db_path_=DATABASE_PATH,
            filename_=FILENAMES[i],
            query_=QUERIES[i]
        )
    print("TRANSFORMATION DONE ✅ 🎉")

###################################################################
########################## EXÉCUTION ##############################
###################################################################
creation()
transformation()