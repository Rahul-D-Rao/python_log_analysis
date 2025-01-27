import pytest
import os
import sys
# Ensure we are in the `src` directory
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src')))
from log_filter import filter_logs_by_level, filter_logs_by_keyword
import pandas as pd

def test_filter_logs_by_level():
    data = {
        'timestamp': ['2023-10-01 10:00:00', '2023-10-01 10:01:00', '2023-10-01 10:02:00'],
        'level': ['INFO', 'ERROR', 'WARNING'],
        'message': ['User logged in', 'Failed login attempt', 'Suspicious activity detected']
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    filtered_df = filter_logs_by_level(df, ['ERROR'])
    
    expected_data = {
        'timestamp': ['2023-10-01 10:01:00'],
        'level': ['ERROR'],
        'message': ['Failed login attempt']
    }
    expected_df = pd.DataFrame(expected_data)
    expected_df['timestamp'] = pd.to_datetime(expected_df['timestamp'])
    
    assert filtered_df.equals(expected_df)

def test_filter_logs_by_keyword():
    data = {
        'timestamp': ['2023-10-01 10:00:00', '2023-10-01 10:01:00', '2023-10-01 10:02:00'],
        'level': ['INFO', 'ERROR', 'WARNING'],
        'message': ['User logged in', 'Failed login attempt', 'Suspicious activity detected']
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    filtered_df = filter_logs_by_keyword(df, ['login'])
    
    expected_data = {
        'timestamp': ['2023-10-01 10:00:00'],
        'level': ['INFO'],
        'message': ['User logged in']
    }
    expected_df = pd.DataFrame(expected_data)
    expected_df['timestamp'] = pd.to_datetime(expected_df['timestamp'])
    
    assert filtered_df.equals(expected_df)