import pandas as pd
import plotly.express as px

adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

vedok_df = adatok[adatok["analysis_role"] == "Defender"].copy()

vedok_df["vedo_pontszam"] = (
    vedok_df["tackles_won"] * 2 
    + vedok_df["interceptions"] * 2 
    + vedok_df["defensive_actions"] * 1
)

top_5_tiszta_vedo = vedok_df.nlargest(5, "vedo_pontszam").copy()

vedo_mutatok = [
    "tackles_won",      # Sikeres szerelések
    "interceptions",    # Labdaszerzések
    "defensive_actions" # Összes védő akció
]

top_5_olvashato = top_5_tiszta_vedo.melt(
    id_vars=["player", "league"],
    value_vars=vedo_mutatok,
    var_name="vedelmi_mutato",
    value_name="ertek",
)

magyar_nevek = {
    "tackles_won": "Sikeres szerelések",
    "interceptions": "Labdaszerzések",
    "defensive_actions": "Összes védő akció",
}
top_5_olvashato["vedelmi_mutato"] = top_5_olvashato["vedelmi_mutato"].map(magyar_nevek)

diagram_tiszta_vedo = px.bar(
    top_5_olvashato,
    x="player",
    y="ertek",
    color="vedelmi_mutato",
    barmode="group",  # Egymás melletti oszlopok a pontos összehasonlításért
    title="5. A Top 5 Tiszta Védő Részletes Teljesítménye",
    labels={
        "player": "Játékos neve",
        "ertek": "Mutató értéke (db)",
        "vedelmi_mutato": "Védekezési mutató",
    },
    hover_name="league",
)

diagram_tiszta_vedo.show()
