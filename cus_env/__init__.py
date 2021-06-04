from gym.envs.registration import register
from copy import deepcopy

from . import datasets


register(
    id='simplestock-v0',
    entry_point='cus_env.envs:CustomEnv',
    kwargs={
        'df': deepcopy(datasets.HDFC),
        'window_size': 24,
        'frame_bound': (24, len(datasets.HDFC))
    }
)
