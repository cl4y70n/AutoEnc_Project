
import numpy as np

def compute_reconstruction_error(original, reconstructed):
    errors = np.mean((original - reconstructed)**2, axis=1)
    return errors

def detect_anomalies(errors, threshold=0.05):
    return errors > threshold
