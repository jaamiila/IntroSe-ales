
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def generate_time(signal, fs):
    duration = len(signal) / fs
    time = np.linspace(0, duration, len(signal))
    return time

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

def detect_activations(binary_signal):
    activations = []
    start = None
    for i in range(len(binary_signal)):
        if binary_signal[i] and start is None:
            start = i
        elif not binary_signal[i] and start is not None:
            activations.append((start, i))
            start = None
    return activations

# Load the data
data = np.genfromtxt("/mnt/data/signal_emg.txt", delimiter="\t", skip_header=3)
y_raw = data[:, -2]
Fs = 1000
time = generate_time(y_raw, Fs)

# Filter the signal
low_c = 2
high_c = 450
y_filtered = butter_bandpass_filter(y_raw - np.mean(y_raw), low_c, high_c, Fs)

# Detect activity and activations
mean_y = np.average(y_filtered)
std_y = np.std(y_filtered)
t_level1 = 1
t_l = mean_y + t_level1 * std_y
binary_signal = np.where(y_filtered >= t_l, int(np.max(y_filtered)), 0)
activations = detect_activations(binary_signal)

# Visualizations (can be commented out if not needed)
plt.figure(figsize=(10, 6))
plt.plot(time, y_filtered, label="EMG filtrado")
for start, end in activations:
    plt.axvspan(time[start], time[end], color='red', alpha=0.3)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Activaciones EMG detectadas")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
