import pandas as pd
import plotly.express as px

adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

poszt_atlag_lapok = (
    adatok.groupby("analysis_role")["yellow_cards"].mean().reset_index()
)
poszt_atlag_lapok.columns = ["analysis_role", "atlag_sarga_lap"]

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

diagram_atlag.show()
