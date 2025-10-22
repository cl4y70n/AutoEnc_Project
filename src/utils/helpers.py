
import matplotlib.pyplot as plt

def plot_anomalies(scores, threshold):
    plt.figure(figsize=(10,5))
    plt.hist(scores, bins=50)
    plt.axvline(threshold, color='r', linestyle='--')
    plt.title('Reconstruction Error Distribution')
    plt.show()
