from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "penjualan.csv")
df["omzet"] = df["jumlah_terjual"] * df["harga_satuan"]

st.set_page_config(page_title="Dashboard UMKM", layout="wide")
st.title("Dashboard Penjualan UMKM")
st.caption("Dataset sintetis untuk demonstrasi analitik dan visualisasi.")

produk = st.selectbox("Pilih produk", ["Semua"] + sorted(df["produk"].unique().tolist()))
filtered = df if produk == "Semua" else df[df["produk"] == produk]
total = int(filtered["omzet"].sum())
unit = int(filtered["jumlah_terjual"].sum())
c1, c2 = st.columns(2)
c1.metric("Total omzet", f"Rp{total:,.0f}")
c2.metric("Total unit terjual", f"{unit:,}")

monthly = filtered.groupby("bulan", as_index=False).agg(omzet=("omzet", "sum"),
                                                        unit=("jumlah_terjual", "sum"))
st.subheader("Tren omzet bulanan")
st.line_chart(monthly.set_index("bulan")["omzet"])
st.subheader("Data yang ditampilkan")
st.dataframe(monthly, use_container_width=True)
st.subheader("Prinsip desain yang digunakan")
st.markdown("- Judul dan label menggunakan bahasa yang jelas.\n- KPI utama ditempatkan di bagian atas.\n- Filter produk memberi kendali kepada pengguna.\n- Grafik garis digunakan untuk menunjukkan perubahan dari waktu ke waktu.")
