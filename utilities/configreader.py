import os
from dotenv import load_dotenv
import json

class ConfigReader:
    dev_mode = True

    @staticmethod
    def set_mode(dev_mode=True):
        ConfigReader.dev_mode = dev_mode
    
    @staticmethod
    def get_mode():
        return ConfigReader.dev_mode

    @staticmethod
    def get_token():
        file_name = 'dev.env' if ConfigReader.dev_mode else 'prod.env'
        env_file = os.path.join(os.path.dirname(__file__), '..', 'project', 'settings', file_name)
        load_dotenv(env_file)
        return os.getenv("TOKEN")
    
    @staticmethod
    def get_config():
        file_name = 'dev.json' if ConfigReader.dev_mode else 'prod.json'
        config_file = os.path.join(os.path.dirname(__file__), '..', 'project', 'settings', file_name)
        with open(config_file, 'r', encoding='utf-8') as config:
            return json.load(config)
