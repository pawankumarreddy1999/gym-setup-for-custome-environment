from gym.envs.registration import register

register(
    id='env_name-v0',
    entry_point='cus_env.envs:CustomEnv',
)
