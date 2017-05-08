import csv
import glob
import os
import sys
from typing import List, Dict, Iterable


def find_log_file():
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
    csvfile = open(log_file, encoding='utf-8-sig')
    reader = csv.DictReader(csvfile)
    return reader


def get_user_log_string(log: Dict[str, List[str]]) -> str:
    return ' '.join(log['user_log'])


def get_message_log_string(log: Dict[str, List[str]]) -> str:
    return ' '.join(log['message_log'])


def read_all_log(reader: Iterable[Dict[str, str]]) -> Dict:
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
