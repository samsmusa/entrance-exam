"""Shared helpers for the 08-statistics graphs.

Every plot script imports this file: it loads the dataset, sets one consistent
look, and saves PNGs into images/08-statistics/.

Run any script from the repo root, e.g.:
    uv run --no-project --with matplotlib --with numpy --with scipy \
        python scripts/08-statistics/01_outliers_number_line.py
or all at once:
    uv run --no-project --with matplotlib --with numpy --with scipy \
        python scripts/08-statistics/make_all.py
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "08-statistics-students.csv"
OUT = ROOT / "images" / "08-statistics"

# Palette (colour-blind-checked order) and neutral inks
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
VIOLET = "#6250d6"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#9a998f"
GRID = "#e4e3de"
SURFACE = "#fcfcfb"
BAND = "#cde2fb"  # light blue for shaded areas


def load():
    """Return the dataset as a dict of numpy arrays (one per column)."""
    with open(DATA, newline="") as f:
        rows = list(csv.DictReader(f))
    num = ["study_hours", "score_before", "score_after", "absences"]
    d = {k: np.array([float(r[k]) for r in rows]) for k in num}
    for k in ["name", "gender", "method", "passed"]:
        d[k] = np.array([r[k] for r in rows])
    return d


def quartiles(x):
    """Q1, Q3 as 'median of lower / upper half' (the method used in the notes)."""
    s = np.sort(x)
    n = len(s)
    lo, hi = s[: n // 2], s[(n + 1) // 2 :]
    return float(np.median(lo)), float(np.median(hi))


def style():
    plt.rcParams.update(
        {
            "figure.facecolor": SURFACE,
            "axes.facecolor": SURFACE,
            "savefig.facecolor": SURFACE,
            "axes.edgecolor": MUTED,
            "axes.labelcolor": INK2,
            "axes.titlecolor": INK,
            "axes.titlesize": 13,
            "axes.titleweight": "bold",
            "axes.titlelocation": "left",
            "axes.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.color": GRID,
            "grid.linewidth": 0.8,
            "axes.axisbelow": True,
            "xtick.color": INK2,
            "ytick.color": INK2,
            "font.size": 10,
            "legend.frameon": False,
            "lines.linewidth": 2,
        }
    )


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("saved", path.relative_to(ROOT))


style()
