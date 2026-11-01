import pandas as pd
import plotly.express as px

adatok = pd.read_csv("elite20_2025_26_league_stats.csv")

bajnoksag_statisztika = adatok["league"].value_counts().reset_index()
bajnoksag_statisztika.columns = ["bajnoksag", "jatek_szam"]

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

diagram1.show()
