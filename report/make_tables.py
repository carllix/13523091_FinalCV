"""Buat tabel LaTeX laporan langsung dari CSV hasil run (desimal koma)."""
import sys
import pandas as pd
from pathlib import Path

root = Path(sys.argv[1])
fig, out = root / "figures", root / "report" / "tables"
COND = ["bersih", "gelap_ringan", "gelap_sedang", "blur_ringan", "blur_sedang", "rotasi_ringan", "rotasi_sedang"]
COND_TEX = {"bersih": "Bersih", "gelap_ringan": "Gelap R", "gelap_sedang": "Gelap S", "blur_ringan": "Blur R",
            "blur_sedang": "Blur S", "rotasi_ringan": "Rotasi R", "rotasi_sedang": "Rotasi S"}


def ms(s):  # "74.51 ± 0.01" -> "74,51 $\pm$ 0,01"
    a, b = s.split(" ± ")
    return f"{a.replace('.', ',')} $\\pm$ {b.replace('.', ',')}"


def num(x):
    return f"{x:.2f}".replace(".", ",").replace("-", "$-$")


m = pd.read_csv(root / "metrics.csv")

# Tabel hasil bersih
t = pd.read_csv(fig / "tabel_hasil_bersih.csv")
rows = [f"{r.experiment_id} & {ms(r.accuracy)} & {ms(r.macro_precision)} & {ms(r.macro_recall)} & {ms(r.macro_f1)} \\\\"
        for r in t.itertuples()]
(out / "hasil_bersih.tex").write_text("\n".join(rows) + "\n")

# Tabel F1 tujuh kondisi
t = pd.read_csv(fig / "tabel_f1_kondisi.csv")
rows = [" & ".join([r["experiment_id"]] + [ms(r[c]) for c in COND]) + " \\\\" for _, r in t.iterrows()]
(out / "f1_kondisi.tex").write_text("\n".join(rows) + "\n")

# Tabel ΔF1
t = pd.read_csv(fig / "tabel_delta_f1.csv")
rows = [" & ".join([r["experiment_id"]] + [ms(r[c]) for c in COND[1:]]) + " \\\\" for _, r in t.iterrows()]
(out / "delta_f1.tex").write_text("\n".join(rows) + "\n")

# Tabel konsistensi: mean selisih, tanda † jika arah tidak sama di tiga seed
t = pd.read_csv(fig / "tabel_konsistensi_seed.csv")
labels = {"E2-E1 (augmentasi, 250)": "E2 $-$ E1", "E4-E3 (augmentasi, 1000)": "E4 $-$ E3",
          "E3-E1 (data, tanpa augmentasi)": "E3 $-$ E1", "E4-E2 (data, dengan augmentasi)": "E4 $-$ E2"}
rows = []
for comp, lab in labels.items():
    g = t[t.perbandingan == comp].set_index("test_condition")
    cells = [num(g.loc[c, "mean"]) + ("$^\\dagger$" if g.loc[c, "konsisten"] == "tidak" else "") for c in COND]
    rows.append(" & ".join([lab] + cells) + " \\\\")
(out / "konsistensi.tex").write_text("\n".join(rows) + "\n")

# Tabel macro-F1 test bersih per seed
t = pd.read_csv(fig / "tabel_f1_bersih_per_seed.csv")
rows = [" & ".join([r["experiment_id"]] + [num(r[c]) for c in ["11", "22", "33"]]) + " \\\\" for _, r in t.iterrows()]
(out / "f1_per_seed.tex").write_text("\n".join(rows) + "\n")

# Tabel jumlah sampel
t = pd.read_csv(fig / "tabel_jumlah_sampel.csv", index_col=0)
per_class = t.drop(index="total").iloc[0]
assert (t.drop(index="total") == per_class).all().all()
names = {"train_penuh": "\\emph{Train} penuh", "train_terbatas": "\\emph{Train} terbatas", "validation": "\\emph{Validation}", "test": "\\emph{Test}"}
rows = [f"{names[c]} & {per_class[c]} & {t.loc['total', c]:,} \\\\".replace(",", ".") for c in t.columns]
(out / "jumlah_sampel.tex").write_text("\n".join(rows) + "\n")

print(*(p.name for p in sorted(out.glob("*.tex"))))
