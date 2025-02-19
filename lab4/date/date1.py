#Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date after subtracting five days:", new_date.strftime("%Y-%m-%d"))
