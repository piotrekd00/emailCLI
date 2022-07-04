import csv
import Source
from Mail import Mail


class CsvSource(Source.Source):

    def __init__(self, path, file_type):
        super(CsvSource, self).__init__(path, file_type)

    def fetch_data(self):
        data = []
        with open(self.path) as f:
            csv_reader = csv.reader(f, delimiter=';')
            next(csv_reader)
            for line in csv_reader:
                d = {'username': line[0], 'mail': line[1]}
                data.append(d)
        return data

    def build_mails(self):
        data = self.fetch_data()
        for user in data:
            if self.filter_mails(user['mail']):
                d = self.split_mail(user['mail'], self.file_type)
                u, m = user['username'], user['mail']
                new_mail = Mail(u, d, m)
                self.mails.append(new_mail)
            else:
                self.incorrect_mails.append(user['mail'])
