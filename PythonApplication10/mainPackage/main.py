# main.py

from APIFinder.apiFinder import *
from FileWriter.writer import *

def main():
    # Initialize the API fetcher with the API key
    meal_fetcher = MealFetcher(api_key="1")
    
    # Fetch the meals data
    meals = meal_fetcher.fetch_meals()
    
    # Display the meals in the console
    meal_fetcher.display_meals(meals)
    
    # Convert the meals data to CSV-compatible format
    csv_data = meal_fetcher.convert_to_csv_format(meals)
    
    # Initialize the CSV writer and write data to a file
    csv_writer = CSVWriter(filename="meals.csv")
    csv_writer.write_to_csv(csv_data)

if __name__ == "__main__":
    main()