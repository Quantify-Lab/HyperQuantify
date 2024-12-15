# main.py
import pandas as pd
from models.data_preparation import prepare_data
from models.lstm_training import train_lstm_model, plot_training_history
from strategies.custom_env import TradingEnv
from strategies.ppo_training import train_ppo_model, evaluate_model

# Load and preprocess data
data = pd.read_csv("market_data.csv")['price'].values
X, y, scaler = prepare_data(data)
X_train, X_val = X[:int(0.8 * len(X))], X[int(0.8 * len(X)):]
y_train, y_val = y[:int(0.8 * len(y))], y[int(0.8 * len(y)):]

# Train LSTM model
lstm_model, history = train_lstm_model(X_train, y_train, X_val, y_val)
plot_training_history(history)

# Reinforcement learning training
env = TradingEnv(data)
rl_model = train_ppo_model(env)
reward = evaluate_model(rl_model, env)

print(f"RL model evaluation reward: {reward}")