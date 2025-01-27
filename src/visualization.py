import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def visualize_logs(parsed_logs_dir):
    """
    Visualizes the filtered log files.
    
    :param parsed_logs_dir: Path to the parsed logs directory.
    """
    log_files = glob.glob(os.path.join(parsed_logs_dir, 'filtered_*.csv'))
    
    if not log_files:
        logging.warning("No filtered log files found for visualization.")
        return
    
    for log_file in log_files:
        df = pd.read_csv(log_file)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Plot log levels over time
        plt.figure(figsize=(14, 7))
        plt.plot(df['timestamp'], df['level'], marker='o', linestyle='-')
        plt.title(f'Log Levels Over Time - {os.path.basename(log_file)}')
        plt.xlabel('Timestamp')
        plt.ylabel('Log Level')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(parsed_logs_dir, f'{os.path.basename(log_file)}.png'))
        plt.close()
        logging.info(f"Visualization saved for {log_file}")

        # Plot log messages over time
        plt.figure(figsize=(14, 7))
        plt.plot(df['timestamp'], df['message'], marker='o', linestyle='-')
        plt.title(f'Log Messages Over Time - {os.path.basename(log_file)}')
        plt.xlabel('Timestamp')
        plt.ylabel('Log Message')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(parsed_logs_dir, f'{os.path.basename(log_file)}_messages.png'))
        plt.close()
        logging.info(f"Message Visualization saved for {log_file}")