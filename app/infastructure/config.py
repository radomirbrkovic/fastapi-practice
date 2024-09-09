from pathlib import Path
import yaml

# Reading and return environment variables for configuration file
def get_config(key: str):
    path = Path("./config.yaml")
    if path.exists():
        with open("./config.yaml") as config_file:
            data = yaml.safe_load(config_file)

        if key in data:
            return data[key]
        else:
            return None

    else:
        return None
