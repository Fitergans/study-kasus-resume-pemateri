from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "penjualan.csv")
df["omzet"] = df["jumlah_terjual"] * df["harga_satuan"]

print("=== Ringkasan omzet per produk ===")
print(df.groupby("produk")["omzet"].agg(["sum", "mean"]).rename(
    columns={"sum": "total_omzet", "mean": "rata_rata_omzet"}).to_string())

print("\n=== Total omzet per bulan ===")
monthly = df.groupby("bulan", as_index=False)["omzet"].sum()
print(monthly.to_string(index=False))

# Baseline tren linear: indeks bulan -> omzet bulanan
X = np.arange(len(monthly)).reshape(-1, 1)
y = monthly["omzet"].to_numpy()
model = LinearRegression().fit(X, y)
next_value = model.predict([[len(monthly)]])[0]
print(f"\nPrediksi baseline omzet bulan berikutnya: Rp{next_value:,.0f}")
print("Catatan: prediksi hanya baseline dari data kecil, bukan jaminan.")
