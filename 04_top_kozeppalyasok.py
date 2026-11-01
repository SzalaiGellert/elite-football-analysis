import pandas as pd
import plotly.express as px

# 1. Lépés: Adatok betöltése a CSV fájlból
adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

# 2. Lépés: SZIGORÚ SZŰRÉS - Csak a középpályások ('Midfielder') jöhetnek szóba!
kozeppalyasok_df = adatok[adatok["analysis_role"] == "Midfielder"].copy()

# 3. Lépés: Középpályás pontszám számítása (kombinálva a támadó és védekező mutatókat)
kozeppalyasok_df["kozeppalyas_pontszam"] = (
    kozeppalyasok_df["assists"] * 3
    + kozeppalyasok_df["tackles_won"] * 2
    + kozeppalyasok_df["interceptions"] * 2
    + kozeppalyasok_df["crosses"] * 1
)

# Kiválasztjuk a Top 5 legjobb középpályást
top_5_kozeppalyas = kozeppalyasok_df.nlargest(5, "kozeppalyas_pontszam").copy()

# 4. Lépés: Mutatók kiválasztása a vizualizációhoz
kp_mutatok = [
    "assists",      # Gólpasszok (készítés)
    "crosses",      # Beadások
    "tackles_won",  # Sikeres szerelések (szűrés)
    "interceptions" # Labdaszerzések
]

# Átalakítjuk a táblázatot a Plotly számára (melt)
top_5_olvashato = top_5_kozeppalyas.melt(
    id_vars=["player", "league"],
    value_vars=kp_mutatok,
    var_name="kp_mutato",
    value_name="ertek",
)

# Szép magyar feliratok a diagramhoz
magyar_nevek = {
    "assists": "Gólpasszok",
    "crosses": "Beadások",
    "tackles_won": "Sikeres szerelések",
    "interceptions": "Labdaszerzések",
}
top_5_olvashato["kp_mutato"] = top_5_olvashato["kp_mutato"].map(magyar_nevek)

# 5. Lépés: Interaktív csoportosított oszlopdiagram készítése
diagram_kp = px.bar(
    top_5_olvashato,
    x="player",
    y="ertek",
    color="kp_mutato",
    barmode="group",  # Egymás melletti oszlopok a pontos összehasonlításért
    title="4. A Top 5 Középpályás Részletes Teljesítménye",
    labels={
        "player": "Játékos neve",
        "ertek": "Mutató értéke (db)",
        "kp_mutato": "Középpályás mutató",
    },
    hover_name="league",
)

# 6. Lépés: Megjelenítés a böngészőben
diagram_kp.show()