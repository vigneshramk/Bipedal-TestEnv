
from gym.envs.registration import register

register(
            id='Bipedal-v0',
                entry_point='gym_bipedal.envs:BipedalEnv',
                max_episode_steps=1600,
                reward_threshold=300,
                )
