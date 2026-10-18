"""The two datasets: where their first-order results are, where the second order is written."""
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent
AGING_RESULTS = PROJECT / "SKA-ECG-Starter-Kit" / "data" / "ecg_ska_results.csv.gz"
PTB_RESULTS = PROJECT / "SKA-ECG-Pathology" / "ska-ecg-engine" / "results"


def folder(ds):
    """aging/ or ptb/, with data/, figures/, vr/."""
    if ds not in ("aging", "ptb"):
        raise SystemExit("dataset: aging or ptb")
    f = ROOT / ds
    for sub in ("data", "figures", "vr"):
        (f / sub).mkdir(parents=True, exist_ok=True)
    return f


def first_order_csv(ds, rec):
    """The file holding the first-order run of this record."""
    return AGING_RESULTS if ds == "aging" else PTB_RESULTS / rec / f"ska_{rec}_runs.csv"


def record(ds, rec):
    return rec.zfill(4) if ds == "aging" else rec


def source(ds, rec):
    """The database line of a description."""
    if ds == "aging":
        sel = pd.read_csv(AGING_RESULTS.parent / "selected_scales.csv", dtype={"record_id": str})
        age = sel.set_index("record_id").age_band.get(rec, "?").replace("-", "–")
        return f"Record {rec}, PhysioNet Autonomic Aging (woman {age}, lead ECG1, 1000 Hz)"
    return f"Record {rec}, PhysioNet PTB Diagnostic ECG Database (lead II, 1000 Hz)"
