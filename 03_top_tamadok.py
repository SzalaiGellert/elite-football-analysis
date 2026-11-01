import pandas as pd
import plotly.express as px

adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

# (A gólokat és gólpasszokat súlyozzuk, hozzáadjuk a lövéseket és beadásokat)
adatok["tamado_pontszam"] = (
    adatok["goals"] * 3
    + adatok["assists"] * 3
    + adatok["shots_on_target"] * 1.5
    + adatok["shots"] * 0.5
    + adatok["crosses"] * 0.2
)

top_5_tamado = adatok.nlargest(5, "tamado_pontszam").copy()

tamado_mutatok = [
    "goals",  # Gólok
    "assists",  # Gólpasszok
    "shots_on_target",  # Kaput eltaláló lövések
    "shots",  # Összes lövés
    "crosses",  # Beadások
]

top_5_olvashato = top_5_tamado.melt(
    id_vars=["player", "league"],
    value_vars=tamado_mutatok,
    var_name="tamado_statisztika",
    value_name="ertek",
)

magyar_nevek = {
    "goals": "Gólok",
    "assists": "Gólpasszok",
    "shots_on_target": "Kaput eltaláló lövések",
    "shots": "Összes lövés",
    "crosses": "Beadások",
}
top_5_olvashato["tamado_statisztika"] = top_5_olvashato[
    "tamado_statisztika"
].map(magyar_nevek)

diagram_tamado = px.bar(
    top_5_olvashato,
    x="player",
    y="ertek",
    color="tamado_statisztika",
    barmode="group",  # Egymás melletti oszlopok a precíz összehasonlításhoz
    title="3. A Top 5 támadó játékos részletes teljesítménye",
    labels={
        "player": "Játékos neve",
        "ertek": "Mutató értéke (db)",
        "tamado_statisztika": "Támadó mutató",
    },
    hover_name="league",
)

diagram_tamado.show()
