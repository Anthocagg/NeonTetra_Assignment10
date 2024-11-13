# utils/file_writer.py

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

