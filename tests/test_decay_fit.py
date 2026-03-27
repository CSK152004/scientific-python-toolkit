import numpy as np
from satool.demo_decay import model
from scipy.optimize import curve_fit

def test_curve_fit_recovers_params_reasonably():
    rng = np.random.default_rng(0)
    A_true, tau_true, C_true = 2.5, 1.7, 0.3
    t = np.linspace(0.0, 6.0, 200)
    sigma = 0.03
    y = model(t, A_true, tau_true, C_true) + rng.normal(0.0, sigma, size=t.shape)

    popt, _ = curve_fit(model, t, y, p0=(2.0, 1.0, 0.0))
    A_fit, tau_fit, C_fit = popt

    assert abs(A_fit - A_true) < 0.2
    assert abs(tau_fit - tau_true) < 0.2
    assert abs(C_fit - C_true) < 0.1
