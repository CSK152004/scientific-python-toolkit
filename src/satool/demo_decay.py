from __future__ import annotations
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def model(t: np.ndarray, A: float, tau: float, C: float) -> np.ndarray:
    return A * np.exp(-t / tau) + C

def run_demo(outdir: Path) -> None:
    rng = np.random.default_rng(42)

    # "True" parameters (ground truth)
    A_true, tau_true, C_true = 2.5, 1.7, 0.3

    # Synthetic data
    t = np.linspace(0.0, 6.0, 80)
    y_clean = model(t, A_true, tau_true, C_true)
    sigma = 0.08
    y = y_clean + rng.normal(0.0, sigma, size=t.shape)

    # Fit
    p0 = (2.0, 1.0, 0.0)
    popt, pcov = curve_fit(model, t, y, p0=p0)
    perr = np.sqrt(np.diag(pcov))
    A_fit, tau_fit, C_fit = popt

    # Save data
    data_path = outdir / "decay_data.csv"
    np.savetxt(data_path, np.c_[t, y], delimiter=",", header="t,y", comments="")

    # Plot
    tt = np.linspace(t.min(), t.max(), 400)
    plt.figure()
    plt.errorbar(t, y, yerr=sigma, fmt=".", capsize=2, label="data")
    plt.plot(tt, model(tt, *popt), label="fit")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Exponential decay fit")
    plt.legend()
    plot_path = outdir / "decay_fit.png"
    plt.tight_layout()
    plt.savefig(plot_path, dpi=200)

    # Print summary (for CLI use)
    print("Fit results:")
    print(f"  A   = {A_fit:.4f} ± {perr[0]:.4f}")
    print(f"  tau = {tau_fit:.4f} ± {perr[1]:.4f}")
    print(f"  C   = {C_fit:.4f} ± {perr[2]:.4f}")
    print(f"Saved: {data_path}")
    print(f"Saved: {plot_path}")
