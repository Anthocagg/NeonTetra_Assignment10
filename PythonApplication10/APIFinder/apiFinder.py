#

import requests
import json

class MealFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = f"https://www.themealdb.com/api/json/v1/{self.api_key}/filter.php?i=chicken_breast"

    def fetch_meals(self):
        """Fetches meal data from the API."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            meals = data.get('meals')
            if meals is None:
                print("No meals found for the specified ingredient.")
                return []
            return meals
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return []

    def convert_to_csv_format(self, meals):
        """Converts meal data to a list of dictionaries suitable for CSV writing."""
        return [{'Meal Name': meal.get("strMeal", "Unknown Meal"), 
                 'Image URL': meal.get("strMealThumb", "No Image Available")}
                for meal in meals]

    def display_meals(self, meals):
        """Prints the meal names and image URLs to the console."""
        if not meals:
            print("No meals to display.")
            return
        print("Chicken Breast Meals Available:\n")
        for meal in meals:
            name = meal.get("strMeal", "Unknown Meal")
            image_url = meal.get("strMealThumb", "No Image Available")
            print(f"Meal Name: {name}")
            print(f"Image URL: {image_url}")
            print("-" * 40)