#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __modification time__ = 2025-01-20
# __author__ = You name, GFZ Helmholtz Centre for Geosciences
# __find me__ = your email and official web


import numpy as np

def calculate_variogram(data, sampling_rate):
    """Calculate the variogram of the input data.

    Args:
        data: Time series data.
        sampling_rate: Sampling rate in Hz.

    Returns:
        A tuple containing time lags and corresponding variogram values.
    """
    max_time_lag = len(data) # why use
    tau_list = np.arange(1, max_time_lag) / sampling_rate
    gamma_tau_list = np.zeros(max_time_lag - 1)

    for delta_t in range(1, max_time_lag):
        shifted_data = data[delta_t:] - data[:-delta_t]
        square_diff = shifted_data ** 2
        gamma_tau_list[delta_t - 1] = np.sum(square_diff) / (2 * len(square_diff))

    return tau_list, gamma_tau_list

def calculate_fractal_dimension(variogram, sampling_rate):
    """Estimate the fractal dimension from a variogram.

    Args:
        variogram: Variogram values.
        sampling_rate: Sampling rate in Hz.

    Returns:
        Estimated fractal dimension (rounded to 3 decimal places).
    """

    tau = np.arange(1, len(variogram) + 1) / sampling_rate
    slope, _ = np.polyfit(np.log10(tau[:4]), np.log10(variogram[:4]), deg=1)
    fractal_dimension = 2 - slope / 2
    return round(fractal_dimension, 3)
