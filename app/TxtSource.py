from .Source import Source
from .Mail import Mail


class TxtSource(Source):

    def fetch_data(self):
        data = []
        with open(self.path) as f:
            for mail in f.readlines():
                if mail.endswith('\n'):
                    data.append(mail[:-1])
                else:
                    data.append(mail)
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

