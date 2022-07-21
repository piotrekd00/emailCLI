class DataEngine:

    def __init__(self, files):
        self.files = files
        self.data = []
        self.incorrect_data = []
        self.get_data()

    def get_data(self):
        for ext in self.files:
            for file in ext:
                file.build_mails()
                self.data += file.mails
                self.incorrect_data += file.incorrect_mails

    def remove_dupes(self):
        self.data = list(dict.fromkeys(self.data))

    def print_data(self):
        print(f'Emails ({len(self.data)})')
        for item in self.data:
            print(f'\t{item.mail}')

    def print_incorrect(self):
        print(f'Invalid emails ({len(self.incorrect_data)})')
        for item in self.incorrect_data:
            print(f'\t{item}')

    def search(self, string):
        result = []
        for item in self.data:
            if string in item.mail:
                result.append(item)
        if len(result) == 0:
            print(f'Sorry, nothing was found :(')
        else:
            print(f"Found emails with '{string}' in email ({len(result)})")
            for item in result:
                print(f'\t{item.mail}')

    def group_by_domain(self):
        result = {}
        for item in self.data:
            if item.domain not in result.keys():
                result[item.domain] = [item.mail]
            else:
                result[item.domain].append(item.mail)

        for key in sorted(result.keys()):
            print(f'Domain {key} ({len(result[key])}):')
            for mail in sorted(result[key]):
                print(f'\t{mail}')

    def read_logs(self, log_path):
        try:
            with open(log_path) as f:
                lines = f.readlines()
                res = ''.join(lines)
        except FileNotFoundError:
            print(f'Sorry, the file was not found...')
        else:
            result = []

            for item in self.data:
                if item.mail not in res:
                    result.append(item.mail)

            print(f'Emails not sent ({len(result)}): ')
            for item in result:
                print(f'\t{item}')
