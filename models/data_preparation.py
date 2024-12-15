# models/data_preparation.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def prepare_data(data, look_back=10):
    """Prepare data for LSTM model."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))

    X, y = [], []
    for i in range(len(scaled_data) - look_back):
        X.append(scaled_data[i:i + look_back, 0])
        y.append(scaled_data[i + look_back, 0])
    X, y = np.array(X), np.array(y)
    return X.reshape(X.shape[0], X.shape[1], 1), y, scaler
