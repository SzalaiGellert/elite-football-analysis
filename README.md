# Elit Futball Adatelemzés (2025/26)

Ez a projekt a 2026-os Aranylabda (Ballon d'Or) 20 kiválasztott jelöltjének 2025/26-os hazai bajnoki szezonbeli teljesítményét elemzi Python, Pandas és Plotly segítségével.

## Az adatsor leírása
Az adatsor (`elite20_2025_26_league_stats.csv`) minden sora egy-egy labdarúgót képvisel, és részletes mutatókat tartalmaz:
- Általános játékos-információk és pozíciók (`analysis_role`)
- Mérkőzések, játékpercek és fegyelmi statisztikák (`matches`, `starts`, `minutes`, `yellow_cards`, `red_cards`)
- Támadó mutatók (`goals`, `assists`, `shots`, `shots_on_target`, `crosses`)
- Védekező akciók (`tackles_won`, `interceptions`, `defensive_actions`)
- Per-90-perces kalkulált mutatók

## Projekt felépítése (Szkriptek)
1. **`01_ligak_eloszlasa.py`**: Elit játékosok megoszlása a bajnokságok szerint.
2. **`02_poszt_atlag_lapok.py`**: Átlagos sárga lapok vizsgálata posztok szerint.
3. **`03_top_tamadok.py`**: A Top 5 támadójátékos részletes teljesítménye.
4. **`04_top_kozeppalyasok.py`**: A Top 5 középpályás komplex mutatói.
5. **`05_top_tiszta_vedok.py`**: A legjobb védők komplex mutatói.
