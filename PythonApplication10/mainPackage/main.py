# Name:  Anthony Caggiano and Ishani Roy Chowdhury
# Email: caggiaaj@mail.uc.edu and roychoii@mail.uc.edu
# Assignment Number:  Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010
# Semester/Year: Fall 24
# Brief Description of the assignment:  This assignment helped us work with APIs, JSON, and CSV in Python. Some things we did were fetching data from an online API,  converting JSON data to a structured format, and saving the structured data to a CSV file. 

# Brief Description of what this module does: This module is ingesting an ingredient from the user and sending it through to find all the meals using that inputed ingredient.
# Citations: https://docs.python.org/3/library/csv.html, https://docs.python.org/3/library/json.html, https://stackoverflow.com/, and https://www.w3schools.com/

# main.py

from APIFinder.apiFinder import *
from FileWriter.writer import *

def main():
    # Prompt the user to enter the ingredient they want to search for
    ingredient = input("Enter an ingredient to search for meals: ")

    # Initialize the API fetcher with the API key
    meal_fetcher = MealFetcher(api_key="1", ingredient=ingredient)
    
    # Fetch the meals data
    meals = meal_fetcher.fetch_meals()

    # Check if any meals were returned
    if not meals:
        print(f"No meals found for: {ingredient}")
        return
    
    # Display the meals in the console
    meal_fetcher.display_meals(meals)
    
    # Convert the meals data to CSV-compatible format
    csv_data = meal_fetcher.convert_to_csv_format(meals)
    
    # Initialize the CSV writer and write data to a file
    csv_writer = CSVWriter(filename="meals.csv")
    csv_writer.write_to_csv(csv_data)

if __name__ == "__main__":
    main()