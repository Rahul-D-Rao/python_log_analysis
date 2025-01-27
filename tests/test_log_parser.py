import pytest
import os
import sys
# Ensure we are in the `src` directory
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src')))
from log_parser import parse_log_file
import pandas as pd

def test_parse_log_file():
    log_content = """[2023-10-01 10:00:00] [INFO] User logged in
[2023-10-01 10:01:00] [ERROR] Failed login attempt"""
    
    with open('test_access.log', 'w') as file:
        file.write(log_content)
    
    df = parse_log_file('test_access.log')
    
    expected_data = {
        'timestamp': ['2023-10-01 10:00:00', '2023-10-01 10:01:00'],
        'level': ['INFO', 'ERROR'],
        'message': ['User logged in', 'Failed login attempt']
    }
    expected_df = pd.DataFrame(expected_data)
    expected_df['timestamp'] = pd.to_datetime(expected_df['timestamp'])
    
    assert df.equals(expected_df)
    
    os.remove('test_access.log')