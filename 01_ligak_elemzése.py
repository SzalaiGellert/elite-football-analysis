import pandas as pd
import plotly.express as px

# 1. Lépés: Adatok betöltése a CSV fájlból
adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

# 2. Lépés: Megszámoljuk a játékosokat bajnokságonként
bajnoksag_statisztika = adatok["league"].value_counts().reset_index()
bajnoksag_statisztika.columns = ["bajnoksag", "jatek_szam"]

# 3. Lépés: Létrehozzuk az interaktív oszlopdiagramot magyar feliratokkal
diagram1 = px.bar(
    bajnoksag_statisztika,
    x="bajnoksag",
    y="jatek_szam",
    title="1. Kiválasztott játékosok eloszlása bajnokságok szerint",
    labels={
        "bajnoksag": "Labdarúgó Bajnokság",
        "jatek_szam": "Játékosok száma (fő)",
    },
    color="bajnoksag",
)

# 4. Lépés: Megjelenítés a böngészőben
diagram1.show()