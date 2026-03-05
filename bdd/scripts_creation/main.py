from database import DBCreation

db = DBCreation("../UE403_DB.db")

FILE_PATHS = {
    0 : "../../donnees/brutes/donnees_geo_climatiques.csv",
    1 : "../../donnees/brutes/donnees_socio_economiques.csv",
    2 : "../../donnees/brutes/mesures_occitanie_journaliere_pollution.csv"
}
TABLE_NAMES = {
    0 : "UE403_Geo_climatiques_provisoire",
    1 : "UE403_Socio_economiques_provisoire",
    2 : "UE403_Mesures_occitanie_journaliere_pollution_provisoire"
}

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