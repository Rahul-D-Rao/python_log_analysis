def filter_logs_by_level(df, levels):
    """
    Filters log entries by a list of log levels.
    
    :param df: DataFrame containing log entries.
    :param levels: List of log levels to filter by (e.g., ['ERROR', 'WARNING']).
    :return: Filtered DataFrame.
    """
    return df[df['level'].isin(levels)]

def filter_logs_by_keyword(df, keywords):
    """
    Filters log entries by a list of keywords in the message.
    
    :param df: DataFrame containing log entries.
    :param keywords: List of keywords to search for in the message.
    :return: Filtered DataFrame.
    """
    return df[df['message'].str.contains('|'.join(keywords), case=False, na=False)]