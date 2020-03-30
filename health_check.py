#!/usr/bin/env python3

import shutil
import psutil

# Complete the script to check the system statistics
# every 60 seconds, and in event of any issues detected among 
# the ones mentioned above, an email should be sent with 
# the following content:

# From: automation@example.com
# To: <user@example.com>
# Subject line: Error - [error message]
# E-mail Body: Please check your system and resolve the issue as soon as possible.
# [error message] will be among the following content:

# CPU usage is over 80%
# Available disk space is less than 20%
# Available memory is less than 500MB
# localhost cannot be resolved to 127.0.0.1

# Note: There is no attachment file here, so you must be careful 
# while defining the generate_email() method in the emails.py script 
# or you can create a separate generate_error_report() method 
# for handling non-attachment email.

