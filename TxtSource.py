from Source import Source
from Mail import Mail


class TxtSource(Source):

    def __init__(self, path, file_type):
        super(TxtSource, self).__init__(path, file_type)

    def fetch_data(self):
        data = []
        with open(self.path) as f:
            for mail in f.readlines():
                data.append(mail[:-1])
        return data

    def build_mails(self):
        data = self.fetch_data()
        for mail in data:
            if self.filter_mails(mail):
                u, d = self.split_mail(mail, self.file_type)
                new_mail = Mail(u, d, mail)
                self.mails.append(new_mail)
            else:
                self.incorrect_mails.append(mail)

