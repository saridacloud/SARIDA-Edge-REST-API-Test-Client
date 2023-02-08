#!/usr/bin/env python3
from configparser import ConfigParser

def defaultConfig() -> ConfigParser:
    config = ConfigParser()
    config['SWAGGER_CONFIG'] = {}
    swagger_config = config['SWAGGER_CONFIG']
    swagger_config['host'] = 'http://localhost:5000/esicteam/SaridaEdgeAPI/1.4'
    swagger_config['temp_folder_path'] = './tmp'
    return config

def loadConfig(file_path: str = './config/appsettings.ini') -> ConfigParser:
    config = ConfigParser()
    config.read(file_path)
    return config

def saveConfig(config: ConfigParser, file_path: str = './config/appsettings.ini') -> None:
    with open(file_path, 'w') as config_file:
        config.write(config_file)
    
if __name__ == "__main__":
    saveConfig(defaultConfig())