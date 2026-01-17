# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# import datetime
# import time
# today = datetime.date.today()
# timestamp = time.time()

# Import core modules
from datetime import date
from time import time

# Import pip module
from camelcase import CamelCase

# Import custom module
from custom_module_validator import validate_email

# date
print(f"date: {date} - type: {type(date)}")
today = date.today()
print(f"today: {today} - type: {type(today)}")

# time
print(f"time: {time} - type: {type(time)}")
timestamp = time()
print(f"timestamp: {timestamp} - type: {type(timestamp)}")

# camelcase
text = "hello there world!"
print(text)

c = CamelCase()
print(c.hump(text))

# validate email
emails = [
    "+**/test@test.com",
    "test@test.com",
    "asd@asd.asd",
    "...asd@asd.asd",
    "asd@asd@asd.asd",
]


def check_email(e):
    if validate_email(e):
        print(f"Email is valid: {e}")
    else:
        print(f"Email is not valid: {e}")


for email in emails:
    check_email(email)
