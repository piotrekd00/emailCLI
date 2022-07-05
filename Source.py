class Source:

    def __init__(self, path, file_type):
        self.path = path
        self.mails = []
        self.file_type = file_type
        self.incorrect_mails = []

    @staticmethod
    def split_mail(mail, file_type):
        mail = str(mail)
        username, domain = mail.split('@')
        if file_type == 'txt':
            dot_index = username.find('.')
            username = username[:dot_index]
            if domain.endswith('co'):
                domain += 'm'
            return username, domain
        elif file_type == 'csv':
            return domain

    @staticmethod
    def filter_mails(mail):
        if mail.count('@') == 1:
            at_index = mail.find('@')
            dot_index = mail.find('.', at_index)
            end_substring = mail[dot_index+1:]
            end_len = len(mail) - dot_index
            if at_index >= 1 \
                    and dot_index - at_index >= 1 \
                    and end_len in range(1, 6) \
                    and end_substring.isalnum():
                return True

    def fetch_data(self):
        pass

    def build_mails(self):
        pass
