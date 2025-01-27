# Python Log File Analysis for Security Events

This project demonstrates how to parse and filter log files for security events using Python. It provides a structured approach to analyzing log files, making it easier to identify and respond to security incidents.

## Table of Contents

- [Python Log File Analysis for Security Events](#python-log-file-analysis-for-security-events)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Directory Structure](#directory-structure)
  - [Sample Log Files](#sample-log-files)
  - [Source Code](#source-code)
  - [Unit Tests](#unit-tests)
  - [Log Analysis file](#log-analysis-file)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Rahul-D-Rao/python_log_analysis.git
   cd python_log_analysis
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to parse and filter log files:

```bash
python src/main.py
```

This script will process the log files located in the `data/sample_logs` directory and save the filtered results in the `data/parsed_logs` directory.

## Directory Structure

```
python_log_analysis/
│
├── README.md
├── requirements.txt
├── data/
│   ├── sample_logs/
│   │   ├── access.log
│   │   └── system.log
│   └── parsed_logs/
│
├── src/
│   ├── __init__.py
│   ├── log_parser.py
│   ├── log_filter.py
│   ├── utils.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_log_parser.py
│   ├── test_log_filter.py
│   └── test_utils.py
├── README.md
├── log_analysis.py
├── .gitignore
└── File_Structure.txt
```

## Sample Log Files

The `data/sample_logs` directory contains sample log files for demonstration purposes:

- `access.log`: Example access log file.
- `system.log`: Example system log file.

## Source Code

The `src` directory contains the source code for the project:

- `__init__.py`: Makes the `src` directory a package.
- `log_parser.py`: Implements the logic for reading and parsing log files.
- `log_filter.py`: Contains functions to filter log entries based on specific criteria (e.g., error levels, keywords).
- `utils.py`: Houses utility functions that can be reused across different modules.
- `main.py`: The entry point of the application, which orchestrates the parsing and filtering processes.

## Unit Tests

The `tests` directory contains unit tests for each module to ensure the correctness of the implementation:

- `__init__.py`: Makes the `tests` directory a package.
- `test_log_parser.py`: Tests the functionality of `log_parser.py`.
- `test_log_filter.py`: Tests the functionality of `log_filter.py`.
- `test_utils.py`: Tests the utility functions in `utils.py`.

To run the tests, use the following command:

```bash
pytest tests/
```

## Log Analysis file

The `notebooks` directory contains Jupyter Notebooks for interactive exploration and visualization of log data:

- `log_analysis.py`: A python script for performing exploratory data analysis on the log files.

Running of the Log Analysis File is:

```bash
python log_analysis.py
```
