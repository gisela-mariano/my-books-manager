import os

import yaml
from easydict import EasyDict
from src.core.persistence.patterns.singleton import Singleton


class Settings(metaclass=Singleton):
    def __init__(
        self,
    ):
        super().__init__()

    def set_env(self, env_path):
        with open(env_path) as f:
            config = yaml.safe_load(f)

        self.__dict__ = EasyDict(config)

        to_update = {
            key: config[key]
            for key in config.keys()
            if not isinstance(config[key], list) and not isinstance(config[key], dict)
        }
        os.environ.update(to_update)
