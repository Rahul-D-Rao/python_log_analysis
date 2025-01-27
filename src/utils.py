import yaml
import os

def load_config(config_path='config.yaml'):
    """
    Loads the configuration from a YAML file.
    
    :param config_path: Path to the configuration file.
    :return: Configuration dictionary.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_sample_logs_dir(config):
    """
    Returns the path to the sample logs directory.
    
    :param config: Configuration dictionary.
    :return: Path to the sample logs directory.
    """
    return os.path.join(os.path.dirname(__file__), '..', config['sample_logs_dir'])

def get_parsed_logs_dir(config):
    """
    Returns the path to the parsed logs directory.
    
    :param config: Configuration dictionary.
    :return: Path to the parsed logs directory.
    """
    return os.path.join(os.path.dirname(__file__), '..', config['parsed_logs_dir'])