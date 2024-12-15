# strategies/ai_market_maker.py
def ai_market_making(model, current_price, position_size):
    """Use trained RL model for market-making decisions."""
    state = np.array([current_price, position_size]).reshape(1, -1)
    action, _ = model.predict(state, deterministic=True)
    bid_price = current_price - action[0] * 0.01
    ask_price = current_price + action[0] * 0.01
    return {"bid_price": bid_price, "ask_price": ask_price}
