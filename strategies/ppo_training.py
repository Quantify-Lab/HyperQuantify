# strategies/ppo_training.py
def train_ppo_model(env, timesteps=10000):
    """Train a PPO model on the trading environment."""
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=timesteps)
    return model


	# •	evaluate_model:
	# •	Evaluates the trained model by running it in the environment for a specified number of episodes.
	# •	Returns the average reward over the episodes.

def evaluate_model(model, env, episodes=10):
    """Evaluate the PPO model over multiple episodes."""
    rewards = []
    for _ in range(episodes):
        obs = env.reset()
        episode_reward = 0
        done = False
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, _ = env.step(action)
            episode_reward += reward
        rewards.append(episode_reward)
    return np.mean(rewards)
