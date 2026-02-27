from database import DBCreation

db = DBCreation("../UE403_DB.db")

FILE_PATHS = {
    0 : "../../donnees/brutes/donnees_geo_climatiques.csv",
    1 : "../../donnees/brutes/donnees_socio_economiques.csv",
    2 : "../../donnees/brutes/mesures_occitanie_journaliere_pollution.csv"
}
TABLE_NAMES = {
    0 : "UE403_Geo_climatique",
    1 : "UE403_Socio_economiques",
    2 : "UE403_Mesures_occitanie_journaliere_pollution"
}

for i in range(len(FILE_PATHS)):
    db.create_table(filepath_=FILE_PATHS[i], table_name_=TABLE_NAMES[i])
    db.insert_values(filepath_=FILE_PATHS[i], table_name_=TABLE_NAMES[i])

# db.drop_table("UE403_Geo_climatique")
# db.drop_table("UE403_Socio_economiques")
# db.drop_table("UE403_Mesures_occitanie_journaliere_pollution")