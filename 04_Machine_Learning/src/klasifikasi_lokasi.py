from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "lokasi_latih.csv")
features = ["kepadatan_penduduk", "biaya_sewa_juta", "akses_jalan",
            "fasilitas_umum", "keamanan"]
X, y = df[features], df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42, stratify=y)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(f"Akurasi data uji: {accuracy_score(y_test, pred):.2f}")
print("\nLaporan klasifikasi:")
print(classification_report(y_test, pred, zero_division=0))

kandidat_baru = pd.DataFrame([{
    "kepadatan_penduduk": 7,
    "biaya_sewa_juta": 2.8,
    "akses_jalan": 8,
    "fasilitas_umum": 7,
    "keamanan": 8
}])
print("Prediksi kandidat contoh:", model.predict(kandidat_baru)[0])
print("Penting: dataset kecil dan label sintetis; model ini hanya contoh alur ML.")
