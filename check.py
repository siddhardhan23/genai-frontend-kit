import os
from utils.config import app_config, env_config
from utils.logger import logger

print(app_config)
print(env_config)
print(os.environ["APP_API_KEY"])
