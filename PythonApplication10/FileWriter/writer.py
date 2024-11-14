# Name:  Anthony Caggiano and Ishani Roy Chowdhury
# Email: caggiaaj@mail.uc.edu and roychoii@mail.uc.edu
# Assignment Number:  Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010
# Semester/Year: Fall 24
# Brief Description of the assignment:  This assignment helped us work with APIs, JSON, and CSV in Python. Some things we did were fetching data from an online API,  converting JSON data to a structured format, and saving the structured data to a CSV file. 

# Brief Description of what this module does: This module is ensuring that the data collected can be put into an easily readable csv file.
# Citations: https://docs.python.org/3/library/csv.html, https://docs.python.org/3/library/json.html, https://stackoverflow.com/, and https://www.w3schools.com/# utils/file_writer.py

import csv

class CSVWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write_to_csv(self, data):
        """Writes a list of dictionaries to a CSV file."""
        if not data:
            print("No data available to write.")
            return
        # Extract headers from the keys of the first dictionary
        headers = data[0].keys()
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully written to {self.filename}")

