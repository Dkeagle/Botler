# Loading modules
from datetime import datetime

# Functions
def log_time():
	# Format the current datetime
	return datetime.now().strftime("[%Y/%m/%d %H:%M:%S.%f]")

# TODO different log commands, for errors, warnings, notices and commands

if __name__ == "__main__":
	print("[1;31m This module is part of the MogBot project and should not be used alone. Try starting bot.py")