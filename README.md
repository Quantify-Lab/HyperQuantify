# HyperQuantify - Smart Trading System

HyperQuantify is an intelligent trading system based on **deep learning** and **reinforcement learning**, designed to implement **time-series forecasting**, **market making**, and **risk management** strategies for automated trading. The system combines **LSTM** (Long Short-Term Memory) and **PPO** (Proximal Policy Optimization) algorithms to predict market prices and make dynamic trading decisions.

## Project Goal

The goal of the HyperQuantify project is to provide a smart trading solution for financial markets. The system collects real-time market data, performs price predictions, implements market-making strategies, and dynamically adjusts positions to manage risk, all while aiming to maximize profit and minimize risk.

## Key Features

1. **[Real-time Data Collection and Storage](https://github.com/Quantify-Lab/HyperQuantify/blob/main/data/live_data_collector.py)**
   - Periodically fetch market data (such as price, volume, etc.) from the Hyperliquid API.
   - Store the collected market data in a local SQLite database for further use.

2. **[Time-Series Forecasting (LSTM)](https://github.com/Quantify-Lab/HyperQuantify/blob/main/models/lstm_training.py)**
   - Use LSTM (Long Short-Term Memory) networks to predict future market prices.
   - Preprocess historical data and format it for LSTM model input.
   - Train the LSTM model to generate future price predictions.

3. **[Reinforcement Learning (PPO)](https://github.com/Quantify-Lab/HyperQuantify/blob/main/strategies/ppo_training.py)**
   - Train a PPO (Proximal Policy Optimization) reinforcement learning model to execute trading decisions (buy, sell, hold).
   - Implement a custom market-making environment (`MarketMakingEnv`) where the agent generates buy/sell quotes based on current market data and position size.

4. **[Dynamic Position Adjustment and Risk Management](https://github.com/Quantify-Lab/HyperQuantify/blob/main/models/risk_management.py)**
   - Use maximum drawdown and volatility to dynamically adjust the position size, controlling trading risks.
   - Adjust the position size based on current market conditions and the maximum drawdown value, ensuring that risks are kept within acceptable limits.

5. **[Visualization Dashboard](https://github.com/Quantify-Lab/HyperQuantify/blob/main/ui/dashboard.py)**
   - Build a simple web-based dashboard using **Flask** to visualize real-time market data.
   - Fetch the latest market data from the SQLite database and display it on a web page.
   - Provide a live view of the market data to help users monitor market movements and system performance.

## Installation and Running

### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Create and initialize the database:
    ```sql
    CREATE TABLE market_data (
        timestamp TEXT,
        price REAL,
        volume REAL
    );
    ```

2. Ensure that market data is filled in the database (you can populate this using data from the Hyperliquid API or any other market data source).

### Running the Application

1. **Start the Data Collection Service**:
   Run the following command to start the data collection service:
    ```bash
    python data/live_data_collector.py
    ```

2. **Train the Model**:
   Train the PPO model using the custom reinforcement learning environment:
    ```bash
    python strategies/ppo_training.py
    ```

3. **Start the Flask Dashboard**:
   Start the Flask web application and visit `http://127.0.0.1:5000/` to view the live market data:
    ```bash
    python ui/dashboard.py
    ```

### Training the Reinforcement Learning Model

1. **Create the Trading Environment**: Use the `TradingEnv` or `MarketMakingEnv` to initialize the custom trading environment.
2. **Train the PPO Model**:
   Train the PPO model with the environment and training timesteps:
    ```python
    from strategies.ppo_training import train_ppo_model
    env = MarketMakingEnv(data)
    trained_model = train_ppo_model(env, timesteps=20000)
    ```

3. **Model Evaluation**: Evaluate the trained model's performance using the `evaluate_model()` function:
    ```python
    from strategies.ppo_training import evaluate_model
    avg_reward = evaluate_model(trained_model, env, episodes=10)
    print(f"Average Reward: {avg_reward}")
    ```

## Project Structure

```text
HyperQuantify/
│
├── data/                    # Data collection and storage related files
│   ├── live_data_collector.py  # Fetches market data and stores it in the database
│
├── models/                  # Deep learning model files
│   ├── data_preparation.py   # Data preprocessing and LSTM input preparation
│   ├── lstm_training.py      # LSTM model training
│   ├── predictor.py          # LSTM time-series forecasting
│   ├── risk_management.py    # Risk management and position adjustment
│
├── strategies/              # Trading strategy related files
│   ├── custom_env.py         # Custom reinforcement learning environment
│   ├── ppo_training.py      # PPO reinforcement learning model training and evaluation
│   ├── ai_market_maker.py   # Market making decision logic
│
├── ui/                      # Frontend related files
│   ├── dashboard.py         # Flask application for displaying market data
│   └── templates/
│       └── dashboard.html   # Web template for displaying market data
│
├── requirements.txt         # Python package dependencies
└── README.md                # Project description and instructions
