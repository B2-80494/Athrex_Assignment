import logging
import logging.handlers
import threading


class CustomLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('CustomLogger')
        self.logger.setLevel(logging.DEBUG)

        # rotating file handler
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=10)
        handler.setLevel(logging.DEBUG)

        # this is a custom formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(threadName)s - %(message)s')
        handler.setFormatter(formatter)

        # handler being added to the logger
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


# example
logger = CustomLogger('test_log.log')


def some_function():
    logger.info('info message')


if __name__ == "__main__":
    logger.debug('debug message')
    logger.error('error message')
    some_function()


    # multithreading
    def threaded_function():
        logger.info('message from thread')


    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
