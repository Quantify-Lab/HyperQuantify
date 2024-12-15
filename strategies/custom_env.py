# strategies/custom_env.py
import gym
from gym import spaces
import numpy as np


class TradingEnv(gym.Env):
    def __init__(self, data, initial_balance=10000):
        super(TradingEnv, self).__init__()
        self.data = data
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Define action and observation spaces
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(3,), dtype=np.float32)

    def reset(self):
        """Reset the environment to the initial state."""
        self.balance = self.initial_balance
        self.current_step = 0
        return self._get_observation()

    def step(self, action):
        """Execute an action and return the new state, reward, and done status."""
        current_price = self.data[self.current_step]
        price_change = action[0] * 0.01
        next_price = current_price * (1 + price_change)
        reward = next_price - current_price
        self.balance += reward
        self.current_step += 1

        done = self.current_step >= len(self.data) - 1
        return self._get_observation(), reward, done, {}

    def _get_observation(self):
        """Return the current observation."""
        return np.array([self.data[self.current_step], self.balance, self.current_step])
