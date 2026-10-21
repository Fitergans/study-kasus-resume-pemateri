from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(7)

# Citra sintetis 100 x 100: nilai indeks vegetasi sebelum dan sesudah.
before = rng.normal(0.72, 0.08, (100, 100)).clip(0, 1)
after = before.copy()

# Simulasikan area perubahan pada beberapa blok. Ini bukan observasi nyata.
after[20:40, 15:45] -= 0.38
after[60:75, 65:85] -= 0.25
after = after.clip(0, 1)
change = before - after
threshold = 0.20
alert = change >= threshold

pixels = pd.DataFrame({
    "row": np.repeat(np.arange(100), 100),
    "col": np.tile(np.arange(100), 100),
    "index_before": before.ravel(),
    "index_after": after.ravel(),
    "decrease": change.ravel(),
    "alert": alert.ravel()
})
out = ROOT / "output"
out.mkdir(exist_ok=True)
pixels.to_csv(out / "pixel_alerts.csv", index=False)

total = alert.size
changed = int(alert.sum())
summary = pd.DataFrame([{
    "total_pixel": total,
    "pixel_alert": changed,
    "persentase_pixel_alert": round(changed / total * 100, 2),
    "ambang_penurunan": threshold
}])
summary.to_csv(out / "summary.csv", index=False)
print(summary.to_string(index=False))
print(f"File keluaran disimpan di: {out}")
print("PERINGATAN: citra sintetis untuk pembelajaran; tidak menunjukkan deforestasi nyata.")
