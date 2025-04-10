import numpy as np

def calculate_variogram(data, sampling_rate):
    max_time_lag = len(data)
    tau_list = np.arange(1, max_time_lag) / sampling_rate  
    gamma_tau_list = np.zeros(max_time_lag - 1)

    for delta_t in range(1, max_time_lag):
        shifted_data = data[delta_t:] - data[:-delta_t]
        square_diff = shifted_data ** 2
        gamma_tau_list[delta_t - 1] = np.sum(square_diff) / (2 * len(square_diff))

    return tau_list, gamma_tau_list

def calculate_fractal_dimension(variogram, sampling_rate):
    tau = np.arange(1, len(variogram) + 1) / sampling_rate
    slope, _ = np.polyfit(np.log10(tau[:4]), np.log10(variogram[:4]), deg=1)
    fractal_dimension = 2 - slope / 2
    return round(fractal_dimension, 3)
