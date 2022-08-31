import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from app.scripts import get_files
from TestDataEngine import TestDataEngine

class TestFeatures(unittest.TestCase):
    
    def setUp(self):
        self.files = get_files("../emails")
        self.engine = TestDataEngine(self.files)
        self.engine.remove_dupes()
    
    def test_incorrect(self):
        actual = self.engine.get_incorrect()
        result = []
        with open("task_1_answer.txt") as f:
            for mail in f.readlines():
                if mail.endswith('\n'):
                    result.append(mail[:-1])
                else:
                    result.append(mail)
        self.assertListEqual(sorted(actual), sorted(result))

    def test_search(self):
        actual = self.engine.search('agustin')
        result = []
        with open("task_2_answer.txt") as f:
            for mail in f.readlines():
                if mail.endswith('\n'):
                    result.append(mail[:-1])
                else:
                    result.append(mail)
        self.assertListEqual(sorted(actual), sorted(result))

    def test_group(self):
        actual = self.engine.group_by_domain()
        result = []
        with open("task_3_answer.txt") as f:
            for mail in f.readlines():
                if mail.endswith('\n'):
                    result.append(mail[:-1])
                else:
                    result.append(mail)
        self.assertListEqual(actual, result)

    def test_logs(self):
        actual = self.engine.read_logs("../email-sent.logs")
        result = []
        with open("task_4_answer.txt") as f:
            for mail in f.readlines():
                if mail.endswith('\n'):
                    result.append(mail[:-1])
                else:
                    result.append(mail)
        self.assertListEqual(sorted(actual), sorted(result))

if __name__ == '__main__':
    unittest.main()