
import streamlit as st
import pandas as pd
from src.anomaly_detection.detect import compute_reconstruction_error, detect_anomalies
from src.utils.helpers import plot_anomalies

st.title('AutoEnc - Fraud Detection Dashboard')

uploaded_file = st.file_uploader('Upload CSV', type='csv')
threshold = st.slider('Threshold', 0.0, 1.0, 0.05)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Exemplo de placeholders de reconstrução (simulação)
    reconstructed = df.values * 0.95
    errors = compute_reconstruction_error(df.values, reconstructed)
    anomalies = detect_anomalies(errors, threshold=threshold)
    st.write('Número de transações suspeitas:', anomalies.sum())
    plot_anomalies(errors, threshold)
