import pandas as pd
import re

import pandas as pd
import re

def parse_log_file(file_path):
    """
    Parses a log file and returns a DataFrame containing the log entries.
    
    :param file_path: Path to the log file.
    :return: DataFrame with parsed log entries.
    """
    # Example log format: [timestamp] [level] message
    log_pattern = re.compile(r'\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(?P<level>[A-Z]+)\] (?P<message>.*)')
    log_entries = []

    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                log_entries.append(match.groupdict())

    df = pd.DataFrame(log_entries)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    return df