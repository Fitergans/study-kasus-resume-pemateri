from pathlib import Path
import pandas as pd
from math import radians, sin, cos, asin, sqrt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "lokasi.csv")
fac = df[df["jenis"] == "fasilitas"].iloc[0]
candidates = df[df["jenis"] == "kandidat"].copy()

def haversine(lat1, lon1, lat2, lon2):
    r = 6371.0
    dlat, dlon = radians(lat2-lat1), radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return 2*r*asin(sqrt(a))

candidates["jarak_km"] = candidates.apply(
    lambda row: haversine(row.latitude, row.longitude, fac.latitude, fac.longitude), axis=1)
candidates = candidates.sort_values("jarak_km")
print("Jarak kandidat ke fasilitas kesehatan (garis lurus):")
print(candidates[["nama_lokasi", "latitude", "longitude", "jarak_km"]].to_string(
    index=False, formatters={"jarak_km": "{:.3f}".format}))
print("\nPeringkat jarak terdekat bukan keputusan lokasi final; pertimbangkan sewa, akses jalan, keamanan, dan kepadatan.")
