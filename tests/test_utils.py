import pytest
import os
import sys
# Ensure we are in the `src` directory
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src')))
from utils import get_sample_logs_dir, get_parsed_logs_dir

def test_load_config():
    config = load_config()
    assert 'sample_logs_dir' in config
    assert 'parsed_logs_dir' in config
    assert 'filter_criteria' in config

def test_get_sample_logs_dir():
    config = load_config()
    expected_path = os.path.join(os.path.dirname(__file__), '..', config['sample_logs_dir'])
    assert get_sample_logs_dir(config) == expected_path

def test_get_parsed_logs_dir():
    config = load_config()
    expected_path = os.path.join(os.path.dirname(__file__), '..', config['parsed_logs_dir'])
    assert get_parsed_logs_dir(config) == expected_path