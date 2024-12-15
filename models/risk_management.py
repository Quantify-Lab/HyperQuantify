# models/risk_management.py
import numpy as np

def calculate_max_drawdown(prices):
    """Calculate the maximum drawdown."""
    peak = prices[0]
    max_drawdown = 0
    for price in prices:
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak
        if drawdown > max_drawdown:
            max_drawdown = drawdown
    return max_drawdown

def adjust_position_size(balance, volatility, max_drawdown, risk_tolerance=0.02):
    """Adjust position size based on risk tolerance and volatility."""
    risk_factor = 1 - min(max_drawdown, risk_tolerance)
    position_size = balance * risk_factor / (volatility + 1e-5)
    return max(0, position_size)

if __name__ == "__main__":
    prices = [100, 102, 101, 98, 99, 95]
    max_dd = calculate_max_drawdown(prices)
    position = adjust_position_size(balance=10000, volatility=0.03, max_drawdown=max_dd)
    print(f"Suggested position size: {position}")