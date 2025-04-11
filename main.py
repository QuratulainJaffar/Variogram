#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __modification time__ = 2025-01-20
# __author__ = You name, GFZ Helmholtz Centre for Geosciences
# __find me__ = your email and official web

import obspy
import numpy as np
import time
from datetime import timedelta

# <editor-fold desc="add the sys.path to search for custom modules">
from pathlib import Path
current_dir = Path(__file__).resolve().parent
# using ".parent" on a "pathlib.Path" object moves one level up the directory hierarchy
project_root = current_dir # .parent
import sys
sys.path.append(str(project_root))
# </editor-fold>

# import the custom functions
from processing import calculate_variogram, calculate_fractal_dimension
from plotting import plot_seismic_and_fd

def main():
    file_path = "/.." ## input file path SAC format # you can use f"{current_dir or project_root}/to/where/you/want"
    output_path = "/.." ## output file path txt format

    st = obspy.read(file_path)
    data = np.concatenate([tr.data for tr in st])
    sampling_rate = st[0].stats.sampling_rate
    start_datetime = st[0].stats.starttime.datetime

    window_duration = 60
    window_size = int(window_duration * sampling_rate)
    time_axis = [start_datetime + timedelta(seconds=i / sampling_rate) for i in range(len(data))]

    fractal_dimensions = []
    time_labels = []
    results = []
    start_time = time.time()

    for step in range(1, len(data) // window_size):
        step_start = start_datetime + timedelta(seconds=window_duration * step - 1)
        start_idx = (step - 1) * window_size
        end_idx = min(start_idx + window_size, len(data))
        segment = data[start_idx:end_idx]

        if len(segment) >= 2:
            tau, gamma = calculate_variogram(segment, sampling_rate)
            fd = calculate_fractal_dimension(gamma, sampling_rate)
        else:
            fd = None

        fractal_dimensions.append(fd)
        time_labels.append(step_start)
        results.append(f"{step_start}, {fd}\n")

    with open(output_path, 'a') as f:
        f.writelines(results)

    plot_seismic_and_fd(time_axis, data, time_labels, fractal_dimensions)

    elapsed = (time.time() - start_time) / 60
    print(f"Elapsed Time: {elapsed:.2f} minutes")

if __name__ == "__main__":
    main()
