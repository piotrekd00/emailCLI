
class TestDataEngine:

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

    def get_incorrect(self):
        result = []
        result.append(f'Invalid emails ({len(self.incorrect_data)}):')
        for item in self.incorrect_data:
            result.append(f'        {item}')
        return result

    def search(self, string):
        search = []
        result = []
        for item in self.data:
            if string in item.mail:
                search.append(item)
        if len(search) == 0:
            result.append(f'Sorry, nothing was found :(')
        else:
            result.append(f"Found emails with '{string}' in email ({len(search)}):")
            for item in search:
                result.append(f'        {item.mail}')
        return result

    def group_by_domain(self):
        group = {}
        result = []
        for item in self.data:
            if item.domain not in group.keys():
                group[item.domain] = [item.mail]
            else:
                group[item.domain].append(item.mail)

        for key in sorted(group.keys()):
            result.append(f'Domain {key} ({len(group[key])}):')
            for mail in sorted(group[key]):
                result.append(f'    {mail}')
        return result

    def read_logs(self, log_path):
        result = []
        try:
            with open(log_path) as f:
                lines = f.readlines()
                res = ''.join(lines)
        except FileNotFoundError:
            print(f'Sorry, the file was not found...')
        else:
            search = []

            for item in self.data:
                if item.mail not in res:
                    search.append(item.mail)

            result.append(f'Emails not sent ({len(search)}):')
            for item in search:
                result.append(f'    {item}')
        return result