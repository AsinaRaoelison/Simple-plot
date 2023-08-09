import argparse
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

def load_geojson(file_path):
    return gpd.read_file(file_path)

def generate_fireplot(geojson_data):
    # Ici, vous devriez charger vos données réelles de départs de feux par an dans la zone
    # Pour cet exemple, nous allons utiliser des données fictives
    data = {
        "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "FireCount": [50, 70, 60, 85, 90, 120, 100, 110, 130, 95, 105]
    }

    df = pd.DataFrame(data)
    df.set_index("Year", inplace=True)
    
    plt.figure(figsize=(10, 6))
    df["FireCount"].plot(kind="bar", color="orange")
    plt.title("Number of Fires per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Fires")
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Generate a fireplot from GeoJSON data.")
    parser.add_argument("-p", "--polygon", required=True, help="Path to the GeoJSON file")
    args = parser.parse_args()

    polygon_data = load_geojson(args.polygon)

    # Vérification du polygone dans Madagascar (hypothétique vérification)
    # Ici, vous devrez implémenter une vérification en utilisant les coordonnées du polygone et les limites de Madagascar
    # Si le polygone n'est pas dans Madagascar, vous pouvez afficher un message d'erreur et quitter le programme

    generate_fireplot(polygon_data)

if __name__ == "__main__":
    main()
