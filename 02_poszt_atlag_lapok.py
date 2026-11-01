import pandas as pd
import plotly.express as px

# 1. Lépés: Adatok betöltése a CSV fájlból
adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

# 2. Lépés: Az átlagos sárga lapok kiszámítása posztonként (játékosonkénti átlag)
poszt_atlag_lapok = (
    adatok.groupby("analysis_role")["yellow_cards"].mean().reset_index()
)
poszt_atlag_lapok.columns = ["analysis_role", "atlag_sarga_lap"]

# 3. Lépés: Létrehozzuk az interaktív oszlopdiagramot az átlagokról
diagram_atlag = px.bar(
    poszt_atlag_lapok,
    x="analysis_role",
    y="atlag_sarga_lap",
    title="2. Átlagos sárga lapok száma játékosonként posztok szerint",
    labels={
        "analysis_role": "Játékos posztja",
        "atlag_sarga_lap": "Átlagos sárga lap (db / játékos)",
    },
    color="analysis_role",
)

# 4. Lépés: Megjelenítés a böngészőben
diagram_atlag.show()