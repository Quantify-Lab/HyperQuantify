# strategies/trading_env.py
import gym
from gym import spaces
import numpy as np

class MarketMakingEnv(gym.Env):
    def __init__(self, data, initial_balance=10000):
        super(MarketMakingEnv, self).__init__()
        self.data = data
        self.balance = initial_balance
        self.current_step = 0

        # Action space: price fluctuation (-1, 1) and position size (0, 1)
        self.action_space = spaces.Box(low=np.array([-1, 0]), high=np.array([1, 1]), dtype=np.float32)
        # Observation space: current price, balance, and position
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(3,), dtype=np.float32)

    def reset(self):
        self.balance = 10000
        self.current_step = 0
        return self._get_obs()

    def step(self, action):
        price = self.data[self.current_step]
        price_change, position_size = action
        next_price = price * (1 + price_change * 0.01)
        profit = position_size * (next_price - price)

        self.balance += profit
        self.current_step += 1

        done = self.current_step >= len(self.data) - 1
        reward = profit
        return self._get_obs(), reward, done, {}

    def _get_obs(self):
        return np.array([self.data[self.current_step], self.balance, self.current_step])

if __name__ == "__main__":
    env = MarketMakingEnv(data=[100, 101, 99, 102, 98])
    obs = env.reset()
    print("Initial state:", obs)
