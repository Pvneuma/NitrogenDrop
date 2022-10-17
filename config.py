import yaml


class Config:
    def __init__(self) -> None:
        with open('config.yml', 'r') as f:
            self.config = yaml.safe_load(f)

    def get(self, key: str):
        if key in self.config:
            return self.config[key]
        return None
