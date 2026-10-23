#!/usr/bin/env python3
"""The trajectory of the cycle vector in the 5-axis probability space, seen on 3 axes at a time.

    v_k = (P of P→Q, Q→R, R→S, S→T, T→P), one point per cycle in [0, 1]^5
    the 10 spaces of 3 of the 5 axes (P→Q, Q→R, R→S, S→T, T→P taken 3 at a time), colour = cycle index k
    complexity of the cloud, after the first SKIP cycles (learning phase):
        dimension = participation ratio (Σλ)² / Σλ², λ = eigenvalues of the covariance of v
        spread    = median and 95 % distance of v from the centre of the cloud

Usage
    python complexity/trajectory_3d.py aging 0060 25
        → complexity/ska_0060_scale25_cycle_trajectory_3axes.png,
          complexity/complexity.csv (one row per record, updated)
Requires: <dataset>/data/cycles_<record>_scale<s>.csv (cycle_vectors.py), numpy, pandas, matplotlib
"""
import itertools
import pathlib
import sys

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
from datasets import folder, record                               # noqa: E402

COLS = ["P_PQ", "P_QR", "P_RS", "P_ST", "P_TP"]
NAMES = ["P→Q", "Q→R", "R→S", "S→T", "T→P"]
SKIP = 20


def complexity(v):
    """Dimension and spread of the cloud of cycle vectors."""
    lam = np.linalg.eigvalsh(np.cov(v.T))[::-1]
    d = np.linalg.norm(v - v.mean(0), axis=1)
    return {"cycles": len(v), "dimension": lam.sum() ** 2 / (lam ** 2).sum(),
            "spread_median": np.median(d), "spread_95": np.percentile(d, 95),
            **{"sd_" + c[2:]: x for c, x in zip(COLS, v.std(0))}}


def all_axes(c, rec, scale, fig_dir):
    """The trajectory in each of the 10 spaces of 3 axes, one panel each."""
    fig = plt.figure(figsize=(10, 22))
    for n, ijk in enumerate(itertools.combinations(range(5), 3)):
        ax = fig.add_subplot(5, 2, n + 1, projection="3d")
        ax.set_box_aspect(None, zoom=.85)
        y = c[[COLS[i] for i in ijk]].to_numpy(float)
        ax.plot(*y.T, lw=.3, color="#999999", alpha=.6)
        ax.scatter(*y.T, c=c.k, s=3, cmap="viridis")
        for a, i in zip((ax.set_xlabel, ax.set_ylabel, ax.set_zlabel), ijk):
            a("P " + NAMES[i], fontsize=8, labelpad=1)
        ax.tick_params(labelsize=6, pad=0)
    fig.suptitle(f"Record {rec}, scale {scale:g}: trajectory of v = (P of P→Q, Q→R, R→S, S→T, T→P) "
                 "\nin the 10 spaces of 3 of the 5 axes (colour = cycle index k)")
    fig.tight_layout()
    out = fig_dir / f"ska_{rec}_scale{scale:g}_cycle_trajectory_3axes.png"
    fig.savefig(out, dpi=120)
    plt.close(fig)
    print(f"saved {out}")


def main():
    ds, rec, scale = sys.argv[1], sys.argv[2], float(sys.argv[3])
    rec, f = record(ds, rec), folder(ds)
    c = pd.read_csv(f / "data" / f"cycles_{rec}_scale{scale:g}.csv")
    v = c[COLS].to_numpy(float)
    all_axes(c, rec, scale, HERE)
    row = {"dataset": ds, "record": rec, "scale": scale, **complexity(v[SKIP:])}
    csv = HERE / "complexity.csv"
    t = pd.read_csv(csv, dtype={"record": str}) if csv.exists() else pd.DataFrame()
    if not t.empty:
        t = t[~((t.dataset == ds) & (t.record == rec) & (t.scale == scale))]
    pd.concat([t, pd.DataFrame([row])]).to_csv(csv, index=False, float_format="%.4g")
    print(f"dimension {row['dimension']:.2f}, spread median {row['spread_median']:.4f}, 95 % {row['spread_95']:.4f}")


if __name__ == "__main__":
    main()
