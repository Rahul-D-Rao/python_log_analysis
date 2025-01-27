from log_parser import parse_log_file
from log_filter import filter_logs_by_level, filter_logs_by_keyword
from utils import load_config, get_sample_logs_dir, get_parsed_logs_dir
from visualization import visualize_logs
import os
import logging

# Configure logging for user-friendly output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting log processing...")

    # Load configuration
    try:
        config = load_config()
        logging.info("Configuration loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return
    
    # Get directories using utility functions
    sample_logs_dir = get_sample_logs_dir(config)
    parsed_logs_dir = get_parsed_logs_dir(config)

    # Ensure parsed_logs_dir exists
    os.makedirs(parsed_logs_dir, exist_ok=True)
    
    # Check if sample logs directory exists and contains log files
    if not os.path.exists(sample_logs_dir):
        logging.error(f"Sample logs directory does not exist: {sample_logs_dir}")
        return
    elif not os.listdir(sample_logs_dir):
        logging.error(f"No log files found in the directory: {sample_logs_dir}")
        return
    
    logging.info(f"Sample logs directory: {sample_logs_dir}")
    logging.info(f"Parsed logs will be saved in: {parsed_logs_dir}")

    # Load filter criteria from config
    filter_levels = config['filter_criteria']['levels']
    filter_keywords = config['filter_criteria']['keywords']
    logging.info(f"Filter levels set to: {filter_levels}")
    logging.info(f"Filter keywords set to: {filter_keywords}")
    
    # Process each log file
    for log_file in os.listdir(sample_logs_dir):
        if log_file.endswith('.log'):
            file_path = os.path.join(sample_logs_dir, log_file)
            logging.info(f"\nProcessing log file: {log_file}")
            logging.info("-" * 40)
            
            try:
                df = parse_log_file(file_path)
                logging.info(f"Successfully parsed {log_file}. Sample data:\n{df.head()}")
            except Exception as e:
                logging.error(f"Error parsing {log_file}: {e}")
                continue
            
            # Apply filtering criteria
            filtered_df = filter_logs_by_level(df, filter_levels)
            filtered_df = filter_logs_by_keyword(filtered_df, filter_keywords)
            logging.info(f"Filtered data for {log_file}. Sample data:\n{filtered_df.head()}")
            
            # Save filtered log to parsed_logs directory
            output_file = os.path.join(parsed_logs_dir, f'filtered_{log_file}')
            try:
                filtered_df.to_csv(output_file, index=False)
                logging.info(f"Filtered log saved to: {output_file}")
            except Exception as e:
                logging.error(f"Error saving filtered log for {log_file}: {e}")
    
    logging.info("All log files processed successfully. Visualizing results...")

    # Visualize logs
    try:
        visualize_logs(parsed_logs_dir)
        logging.info("Visualization complete.")
    except Exception as e:
        logging.error(f"Error visualizing logs: {e}")

    logging.info("Log processing finished.")

if __name__ == "__main__":
    main()