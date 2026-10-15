# SKA-ECG Second Order

**Second-order SKA learning of the heartbeat: the learner reads its own first-order result, one
step per cycle.**

## From the first order to the second

The first-order SKA learner turns the ECG into five bands, one per transition of the heartbeat
(P→Q, Q→R, R→S, S→T, T→P), each at its own height P = exp(−|ΔH/H|).

1. **Cycle vector** — each cycle k gives v_k = (P of P→Q, Q→R, R→S, S→T, T→P).
2. **Path** — the rank of the five heights in v_k: the order in which the cycle goes up and down
   through the bands.
3. **Scalar product** — c_k = cos(v_k, v_k+1), two successive cycles compared.
4. **Return** — ln(c_k / c_k−1), what the second-order learner reads, one step per cycle.

A heart that repeats the same cycle gives one band. A cycle that differs from the one before
leaves it.

## The second-order axes

| | first order (per transition) | second order (per cycle) |
|---|---|---|
| z₂ | ‖Z‖ of the 5 transitions | ‖Z₂‖ of the returns of c_k |
| Δt₂ | time between two waves | time between two cycles |
| ż₂ | dz/dt | dz₂/dt₂ |
| P₂ | exp(−\|ΔH/H\|), first-order entropy | exp(−\|ΔH₂/H₂\|), second-order entropy |

## Data

- [`aging/`](aging/) — 38 women of the PhysioNet Autonomic Aging database, first order from
  [SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability)
  (Starter-Kit), each at her selected scale.
- [`ptb/`](ptb/) — PhysioNet PTB, lead II, first order from
  [SKA-ECG-Pathology](https://github.com/quantiota/SKA-ECG-Pathology).

Each holds `data/`, `figures/` and `vr/` (one cube per record, links in `vr/README.md`).

## Cubes — Autonomic Aging

One cube per woman: second-order learning (scale 25) of her first-order run at her selected scale.
Axes z₂, ż₂, P₂; colour = the sign of the return. Open in a browser; a headset can enter VR.

| age | record | first-order scale | cube |
|---|---|---|---|
| 20–24 | 0002 | 60 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0002_scale60_scale25_vr.html) |
| 18–19 | 0044 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0044_scale25_scale25_vr.html) |
| 60–64 | 0053 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0053_scale25_scale25_vr.html) |
| 18–19 | 0060 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0060_scale25_scale25_vr.html) |
| 55–59 | 0082 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0082_scale25_scale25_vr.html) |
| 18–19 | 0098 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0098_scale25_scale25_vr.html) |
| 45–49 | 0114 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0114_scale25_scale25_vr.html) |
| 75–79 | 0153 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0153_scale25_scale25_vr.html) |
| 25–29 | 0155 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0155_scale25_scale25_vr.html) |
| 40–44 | 0164 | 40 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0164_scale40_scale25_vr.html) |
| 85–92 | 0188 | 30 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0188_scale30_scale25_vr.html) |
| 65–69 | 0214 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0214_scale25_scale25_vr.html) |
| 70–74 | 0229 | 5 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0229_scale5_scale25_vr.html) |
| 70–74 | 0237 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0237_scale25_scale25_vr.html) |
| 18–19 | 0239 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0239_scale25_scale25_vr.html) |
| 35–39 | 0248 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0248_scale25_scale25_vr.html) |
| 18–19 | 0262 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0262_scale25_scale25_vr.html) |
| 30–34 | 0275 | 70 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0275_scale70_scale25_vr.html) |
| 75–79 | 0276 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0276_scale25_scale25_vr.html) |
| 18–19 | 0290 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0290_scale25_scale25_vr.html) |
| 80–84 | 0312 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0312_scale25_scale25_vr.html) |
| 40–44 | 0314 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0314_scale25_scale25_vr.html) |
| 45–49 | 0395 | 30 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0395_scale30_scale25_vr.html) |
| 50–54 | 0401 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0401_scale35_scale25_vr.html) |
| 65–69 | 0413 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0413_scale35_scale25_vr.html) |
| 55–59 | 0420 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0420_scale35_scale25_vr.html) |
| 18–19 | 0465 | 70 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0465_scale70_scale25_vr.html) |
| 25–29 | 0515 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0515_scale35_scale25_vr.html) |
| 18–19 | 0697 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0697_scale25_scale25_vr.html) |
| 18–19 | 0886 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0886_scale25_scale25_vr.html) |
| 80–84 | 0889 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0889_scale35_scale25_vr.html) |
| 35–39 | 0897 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0897_scale25_scale25_vr.html) |
| 85–92 | 0912 | 35 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0912_scale35_scale25_vr.html) |
| 50–54 | 0936 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0936_scale25_scale25_vr.html) |
| 60–64 | 0942 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_0942_scale25_scale25_vr.html) |
| 30–34 | 1053 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_1053_scale25_scale25_vr.html) |
| 18–19 | 1088 | 25 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_1088_scale25_scale25_vr.html) |
| 20–24 | 1112 | 50 | [open](https://quantiota.github.io/SKA-ECG-Second-Order/aging/vr/ska2_ecg_1112_scale50_scale25_vr.html) |

## Run

```bash
cd scripts
python cycle_vectors.py aging 0060 25            # cycle vectors, path, c_k, return
python learn_second_order.py aging 0060 25 25    # second-order learning (second-order scale 25)
python plot_second_order.py aging 0060 25 25     # figure
python build_cube2.py aging 0060 25 25           # cube
```

The SKA learner itself is not included in this repository.

## License

Scripts: MIT. ECG data: PhysioNet, under the license of each database.
