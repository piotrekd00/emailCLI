import sys
import click
import os
from .CsvSource import CsvSource
from .TxtSource import TxtSource
from pathlib import Path

def get_files(path):
    txt_path = []
    csv_path = []

    if not os.path.isdir(path):
        print("Directory does not exist")
        sys.exit()

    for file in os.listdir(path):
        if file.endswith(".txt"):
            txt_path.append(os.path.join(path, file))
        elif file.endswith(".csv"):
            csv_path.append(os.path.join(path, file))

    txt_files = [TxtSource(path, 'txt') for path in txt_path]
    csv_files = [CsvSource(path, 'csv') for path in csv_path]

    files = [txt_files, csv_files]
    return files


def validate_input(var_dict):
    count = 0

    for var in var_dict.keys():
        if var_dict[var]:
            count += 1

    if count > 1:
        print(f'You passed more than one function, the program will exit')
        raise click.Abort

    if var_dict['find_emails_not_in_logs'] is not None and\
            not var_dict['find_emails_not_in_logs'].endswith('.logs'):
        print(f'File must be of .logs extension!')
        raise click.Abort
