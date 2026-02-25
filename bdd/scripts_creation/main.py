from database import DBQuery

db = DBQuery("../UE403_DB.db")

init_url = "../../donnees/brutes"
db.create_table(filepath_=f"{init_url}/donnees_geo_climatiques.csv", table_name_="UE403_Geo_climatique")
db.create_table(filepath_=f"{init_url}/donnees_socio_economiques.csv", table_name_="UE403_Socio_economiques")
db.create_table(filepath_=f"{init_url}/mesures_occitanie_journaliere_pollution.csv", table_name_="UE403_Mesures_occitanie_journaliere_pollution")

