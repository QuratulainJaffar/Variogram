#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __modification time__ = 2025-01-20
# __author__ = You name, GFZ Helmholtz Centre for Geosciences
# __find me__ = your email and official web


import numpy as np

def calculate_variogram(data, sampling_rate):
    '''
    Say something about the purpose of the funcs, it would be great you give a equation or ref to let the people understand this
    Args:
        data: data type? (int, numpy 1D or 2D array? or list or?), say something about this parameter? otherwise, nore can understnad this
        sampling_rate:

    Returns:
        tau_list: data type? what;s this?
        gamma_tau_list
    '''
    max_time_lag = len(data) # why use
    tau_list = np.arange(1, max_time_lag) / sampling_rate
    gamma_tau_list = np.zeros(max_time_lag - 1)

    for delta_t in range(1, max_time_lag):
        shifted_data = data[delta_t:] - data[:-delta_t]
        square_diff = shifted_data ** 2
        gamma_tau_list[delta_t - 1] = np.sum(square_diff) / (2 * len(square_diff))

    return tau_list, gamma_tau_list

def calculate_fractal_dimension(variogram, sampling_rate):
    '''
    Say something about the purpose of the funcs, it would be great you give a equation or ref to let the people understand this
    Args:
        data: data type? (int, numpy 1D or 2D array? or list or?), say something about this parameter? otherwise, nore can understnad this
        sampling_rate:

    Returns:
        tau_list: data type? what;s this?
        gamma_tau_list
    '''

    tau = np.arange(1, len(variogram) + 1) / sampling_rate
    slope, _ = np.polyfit(np.log10(tau[:4]), np.log10(variogram[:4]), deg=1)
    fractal_dimension = 2 - slope / 2
    return round(fractal_dimension, 3)
