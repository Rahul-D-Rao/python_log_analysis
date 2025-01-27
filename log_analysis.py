import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
# Ensure we are in the `src` directory
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, 'src')))
from utils import load_config, get_parsed_logs_dir
import logging

# Configure logging for user-friendly output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_logs(parsed_logs_dir):
    """
    Analyzes and visualizes the parsed log files.
    
    :param parsed_logs_dir: Path to the parsed logs directory.
    """
    # Get all log files in the directory
    log_files = [f for f in os.listdir(parsed_logs_dir) if f.endswith('.log')]
    
    if not log_files:
        logging.warning("No parsed log files found for analysis in the directory.")
        return
    
    logging.info(f"Found {len(log_files)} log file(s) for analysis: {log_files}")
    
    for log_file in log_files:
        file_path = os.path.join(parsed_logs_dir, log_file)
        logging.info(f"\nStarting analysis for log file: {log_file}")
        
        # Read the log file into a DataFrame
        try:
            df = pd.read_csv(file_path)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            logging.info(f"Successfully loaded {log_file}. Data preview:")
            logging.info(df.head())
        except Exception as e:
            logging.error(f"Error loading log file {log_file}: {e}")
            continue
        
        # Display basic statistics
        logging.info(f"\nDisplaying basic statistics for {log_file}:")
        print(f"\nBasic Statistics for {log_file}:")
        print(df.describe(include='all'))
        
        # Plot log levels over time
        logging.info(f"Plotting log levels over time for {log_file}...")
        plt.figure(figsize=(14, 7))
        plt.plot(df['timestamp'], df['level'], marker='o', linestyle='-')
        plt.title(f'Log Levels Over Time - {log_file}')
        plt.xlabel('Timestamp')
        plt.ylabel('Log Level')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Plot log messages over time
        logging.info(f"Plotting log messages over time for {log_file}...")
        plt.figure(figsize=(14, 7))
        plt.plot(df['timestamp'], df['message'], marker='o', linestyle='-')
        plt.title(f'Log Messages Over Time - {log_file}')
        plt.xlabel('Timestamp')
        plt.ylabel('Log Message')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Load configuration
    try:
        config = load_config()
        logging.info("Configuration loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return
    
    # Get parsed logs directory
    parsed_logs_dir = get_parsed_logs_dir(config)
    logging.info(f"Parsed logs directory: {parsed_logs_dir}")
    
    # Analyze logs
    logging.info("Starting the log analysis process...")
    analyze_logs(parsed_logs_dir)
    logging.info("Log analysis completed.")

if __name__ == "__main__":
    main()