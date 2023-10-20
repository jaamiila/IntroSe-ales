
import numpy as np
import matplotlib.pyplot as plt
import pywt

def wavelet_decomposition(signal, wavelet_type, levels):
    coeffs = pywt.wavedec(signal, wavelet_type, level=levels)
    return coeffs

def plot_signal_and_coefficients(signal, signal_name, color):
    coeffs = wavelet_decomposition(signal, 'db4', 4)
    
    plt.figure(figsize=(20, 15))
    plt.subplot(6, 1, 1)
    plt.plot(signal, color)
    plt.title(f"{signal_name} Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")

    for i, coeff in enumerate(coeffs, start=1):
        plt.subplot(6, 1, i+1)
        plt.plot(coeff)
        if i == 1:
            plt.title(f"{signal_name} - Coefficient cA{len(coeffs)-i}")
        else:
            plt.title(f"{signal_name} - Coefficient cD{len(coeffs)-i}")
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

# Load the signals
ecg = np.genfromtxt("/mnt/data/ecg.txt", delimiter="\t", skip_header=3)[:, -2]
eeg = np.genfromtxt("/mnt/data/eeg.txt", delimiter="\t", skip_header=3)[:, -2]
emg = np.genfromtxt("/mnt/data/emg.txt", delimiter="\t", skip_header=3)[:, -2]

# Plot ECG, EEG and EMG signals with their wavelet coefficients
plot_signal_and_coefficients(ecg, "ECG", 'r')
plot_signal_and_coefficients(eeg, "EEG", 'b')
plot_signal_and_coefficients(emg, "EMG", 'k')
