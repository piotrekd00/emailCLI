from CsvSource import CsvSource
from TxtSource import TxtSource
import os

if __name__ == '__main__':

    txt_path = []
    for file in os.listdir("./emails"):
        if file.endswith(".txt"):
            txt_path.append(os.path.join("emails", file))

    csv_path = []
    for file in os.listdir("./emails"):
        if file.endswith(".csv"):
            csv_path.append(os.path.join("emails", file))

    txt_files = [TxtSource(path, 'txt') for path in txt_path]
    csv_files = [CsvSource(path, 'csv') for path in csv_path]

    data = []
    incorrect_data = []
    search_result = []

    for file in csv_files and txt_files:
        file.build_mails()
        data += file.mails
        incorrect_data += file.incorrect_mails

    for file in csv_files and txt_files:
        search_result += file.search("leann")

    print(data)
    print(incorrect_data)
    print(search_result)
