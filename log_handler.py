import csv
import glob
import os
import sys
from typing import List, Dict, Iterable


def find_log_file():
    """Find kakaotalk chat log file.

    If there is no argument, it will find the latest log file from 'log/' directory.
    Or it uses the given log file.
    """
    args = sys.argv
    if len(args) == 1:
        list_of_chat_log = glob.glob('logs/*.csv')
        latest_chat_log = max(list_of_chat_log, key=os.path.getctime)
        chat_log_file = latest_chat_log
    else:
        chat_log_file = args[1]
        if not os.path.isfile(chat_log_file):
            raise FileNotFoundError(f'{chat_log_file} is not found')
    return chat_log_file


def get_log_reader(log_file: str) -> Iterable[Dict[str, str]]:
    """Getting a reader object for reading the log data from csv format.

    Args:
        log_file: Path of chat log file
    """
    csvfile = open(log_file, encoding='utf-8-sig') # Ignore the first BOM character with 'utf-8-sig'
    reader = csv.DictReader(csvfile)
    return reader


def convert_user_log_to_string(log: Dict[str, List[str]]) -> str:
    """"Convert the user log list to a string.

    Args:
        log: Chat log data
    """
    return ' '.join(log['user_log'])


def convert_message_log_to_string(log: Dict[str, List[str]]) -> str:
    """"Convert the message log list to a string.

    Args:
        log: Chat log data
    """
    return ' '.join(log['message_log'])


def read_all_log(reader: Iterable[Dict[str, str]]) -> Dict:
    """"Read all chat log and get the all rows corresponding to each columns.

    Args:
        reader: A file contents reader for reading the log data
    """
    data = {
        'time_series_log': list(),
        'message_log': list(),
        'user_log': list(),
    }
    for line in reader:
        data['time_series_log'].append(line['Date'])
        data['user_log'].append(line['User'])
        data['message_log'].append(line['Message'])
    return data
