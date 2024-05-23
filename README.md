# Athrex_Assignment
This repository consists of the assignment I am to submit before my internship.

__________Problem Statement__________

Implement a logger module which can collect logs and can be seamlessly integrated into any codebase.
Requirements:

● Log messages are inserted in a file at some well-known location.

● Logs should be saved in the log file in the following format:

○ Timestamp

○ Log Level (Levels could be DEBUG, INFO, ERROR)

○ File name (Source code file from which log was created)

○ Function name (Function name from which log creation was invoked)

○ Thread ID

○ Actual log message

● Log file should be rotated after every 5 MB, with a limit of 10 rotations, after which the old logs will be automatically wrapped around.
Assume that the logger will be running in a multithreaded environment.

There is no barrier to the programming language in which the assignment can be implemented.
____________________



As I am familiar with Python, I have opted to use Python for solving this problem.

Libraries used: logging, os, threading, datetime.

Logging: The logging module in Python is a powerful and flexible system for tracking events that happen when some software runs. 

os: It is a module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.

Threading: The threading module in Python allows us to create and manage threads for concurrent execution of tasks, making our programs more efficient and responsive. With the threading module, we can create threads, manage their execution, and use synchronization mechanisms to ensure safe and predictable behaviour in your multi-threaded programs.

datetime: Python datetime module supplies classes to work with date and time. These classes provide several functions to deal with dates, times, and time intervals. Date and DateTime are an object in Python, so when we manipulate them, we are manipulating objects and not strings or timestamps. 



Files:

1. logger.py

At the beginning of this file, I imported the required libraries I will be using to write the logger module.
Then I defined the class named CustomLogger which inhibits the logger's functionality

CustomLogger Class:

__init__:
This sets up a logger instance with logging.getLogger.
Configures a RotatingFileHandler to rotate logs after 5 MB, keeping up to 10 backup files. Also, applies a custom formatter to log messages, including the timestamp, log level, filename, function name, thread name, and the actual message.

Log Methods:
Provides methods (debug, info, error) to log messages at different levels.

Usage Example:

Demonstrates how to use the CustomLogger class.
Includes a function to show logging from within a function.
Simulates multithreaded logging to ensure thread safety and correct logging of thread IDs.


To integrate this logger module into any codebase:

Import the CustomLogger class.
Initialize the logger with the desired log file path.
Use the logging methods (debug, info, error) provided by the CustomLogger instance.
This implementation ensures that logs are well-structured, easy to read, and manage, even in a multithreaded environment. 
It also handles log file rotation as specified, preventing excessive disk usage and keeping recent log history available.



2. tests.py

To automate the testing of the `CustomLogger` class, I have used Python's unit test framework. I created test cases to verify that the logger correctly logs messages at different levels, rotates the log file as expected, and includes all required information in each log entry.

setUpClass: This sets up a logger instance and logs the file path before any tests run.

tearDownClass: Cleans up log files after all tests are completed.

read_log Method: Reads and returns the content of the log file for verification purposes.

test_debug_log, test_info_log, test_error_log: Verify that debug, info, and error messages are correctly logged and contain the appropriate log level.

test_log_format: This ensures that the log format includes all required parts: timestamp, log level, filename, function name, thread name, and the actual message.

test_log_rotation: Writes enough logs to trigger log rotation and verifies that 10 log files are created.

test_multithreading: Simulates multithreaded logging and verifies that messages from different threads are logged correctly.



For running the tests: 

To run the tests, execute the test_custom_logger.py file. After executing the test_custom_logger.py file it will execute all the test cases and provide output indicating whether each test passed or failed.
