import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

plt.rcParams.update( {'font.size':7,
                      'font.family': "Arial",
                      'axes.formatter.limits': (-3, 3),
                      'axes.formatter.use_mathtext': True} )

def plot_seismic_and_fd(time_axis, data, time_labels, fractal_dimensions):
    '''

    Args:
        time_axis:
        data:
        time_labels:
        fractal_dimensions:

    Returns:

    '''

    fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # Plot 1: Seismic waveform
    ax[0].plot(time_axis, data, 'k-', label='Waveform')
    ax[0].set_title('Seismic Waveform')
    ax[0].set_ylabel('Amplitude (counts)')
    ax[0].ticklabel_format(style='sci', scilimits=(-1, 2), axis='y')
    ax[0].tick_params(axis='x', labelbottom=False)

    # Plot 2: Fractal Dimensions
    valid_fd = [fd for fd in fractal_dimensions if fd is not None]
    ax[1].plot(time_labels[:len(valid_fd)], valid_fd, 'o', color='black', label='Fractal Dimension')
    ax[1].set_title('Fractal Dimensions')
    ax[1].set_ylabel('Fractal Dimension (FD)')
    ax[1].set_ylim(1, 2)
    ax[1].set_xlabel('Time')
    ax[1].legend()

    # Format x-axis
    ax[1].set_xticks(time_labels[::60])
    ax[1].xaxis.set_major_formatter(FixedFormatter([t.strftime("%H:%M") for t in time_labels[::60]]))
    plt.setp(ax[1].xaxis.get_majorticklabels(), rotation=45, ha="right")

    plt.tight_layout()
    plt.show()
