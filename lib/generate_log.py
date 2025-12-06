from datetime import datetime
import os

def generate_log(data):
    """Write log entries to a file named with today's date and return the filename.

    Raises ValueError if log_data is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    return filename
