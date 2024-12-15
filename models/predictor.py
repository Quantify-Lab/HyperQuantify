# models/predictor.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm_model(input_shape):
    """Construct an LSTM model for time series prediction."""
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        LSTM(32),
        Dense(1)
    ])
    # Compile the model using Mean Squared Error loss and Adam optimizer
    model.compile(optimizer='adam', loss='mse')
    return model