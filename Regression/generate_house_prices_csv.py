import pandas as pd
import random

data = []

for _ in range(100):
    land_area = random.randint(50, 200)        # luas tanah (m2)
    rooms = random.randint(2, 6)               # jumlah kamar
    year_built = random.randint(2005, 2023)    # tahun bangun

    # aturan harga sederhana (biar realistis)
    price = (
        land_area * 5 +
        rooms * 50 +
        (year_built - 2000) * 10 +
        random.randint(-50, 50)
    )

    data.append([land_area, rooms, year_built, price])

df = pd.DataFrame(
    data,
    columns=["land_area", "rooms", "year_built", "price"]
)

df.to_csv("house_prices.csv", index=False)
print("house_prices.csv berhasil dibuat (100 data)")
