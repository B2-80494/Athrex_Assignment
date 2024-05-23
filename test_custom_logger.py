import os
import threading
import unittest
from datetime import datetime

from custom_logger import CustomLogger


class TestCustomLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log_file = 'test_log.log'
        cls.logger = CustomLogger(cls.log_file)

    @classmethod
    def tearDownClass(cls):
        # cleaning log files after tests
        for i in range(11):
            log_file = f'{cls.log_file}.{i}' if i > 0 else cls.log_file
            if os.path.exists(log_file):
                os.remove(log_file)

    def read_log(self):
        with open(self.log_file, 'r') as f:
            return f.readlines()

    def test_debug_log(self):
        self.logger.debug('debug message')
        logs = self.read_log()
        self.assertTrue(any('debug message' in log for log in logs))
        self.assertTrue(any('DEBUG' in log for log in logs))

    def test_info_log(self):
        self.logger.info('info message')
        logs = self.read_log()
        self.assertTrue(any('info message' in log for log in logs))
        self.assertTrue(any('INFO' in log for log in logs))

    def test_error_log(self):
        self.logger.error('error message')
        logs = self.read_log()
        self.assertTrue(any('error message' in log for log in logs))
        self.assertTrue(any('ERROR' in log for log in logs))

    def test_log_format(self):
        self.logger.info('test message')
        logs = self.read_log()
        self.assertTrue(any('test message' in log for log in logs))
        for log in logs:
            if 'test message' in log:
                parts = log.split(' - ')
                self.assertEqual(len(parts), 6)
                self.assertTrue(datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S,%f'))
                self.assertIn(parts[1], ['DEBUG', 'INFO', 'ERROR'])
                self.assertTrue(parts[2].endswith('.py'))
                self.assertTrue(len(parts[3]) > 0)
                self.assertTrue(len(parts[4]) > 0)
                self.assertTrue('test message' in parts[5])

    def test_log_rotation(self):
        # write log which will exceed 5MB
        large_message = 'A' * 1024 * 1024
        for _ in range(6):
            self.logger.info(large_message)

        # log rotation
        log_files = [self.log_file] + [f'{self.log_file}.{i}' for i in range(1, 11)]
        existing_logs = [log for log in log_files if os.path.exists(log)]
        self.assertEqual(len(existing_logs), 3)

    def test_multithreading(self):
        def thread_log():
            self.logger.info('logging message')

        threads = []
        for _ in range(5):
            t = threading.Thread(target=thread_log)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        logs = self.read_log()
        self.assertTrue(any('logging message' in log for log in logs))


if __name__ == '__main__':
    unittest.main()
