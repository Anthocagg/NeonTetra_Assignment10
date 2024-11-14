# Name:  Anthony Caggiano and Ishani Roy Chowdhury
# Email: caggiaaj@mail.uc.edu and roychoii@mail.uc.edu
# Assignment Number:  Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010
# Semester/Year: Fall 24
# Brief Description of the assignment:  This assignment helped us work with APIs, JSON, and CSV in Python. Some things we did were fetching data from an online API,  converting JSON data to a structured format, and saving the structured data to a CSV file. 

# Brief Description of what this module does: This module is using the api to find recipe names and images that connet to the user input ingredient from main.py
# Citations: https://docs.python.org/3/library/csv.html, https://docs.python.org/3/library/json.html, https://stackoverflow.com/, and https://www.w3schools.com/

# apiFinder.py

from unicodedata import category
import requests
import json

class MealFetcher:
    def __init__(self, api_key: str, ingredient: str):
        self.api_key = api_key
        self.ingredient = ingredient
        self.url = f"https://www.themealdb.com/api/json/v1/{self.api_key}/filter.php?i={self.ingredient}"

    def fetch_meals(self):
        """Fetches meal data from the API."""
        meals = []
        if self.ingredient:
            ingredient_url = f"{self.url}/filter.php?i={self.ingredient}"
            meals += self.fetch_from_url(ingredient_url)
        if not meals:
            print(f"No meals found for ingredient: {self.ingredient}")
        return meals

    def fetch_from_url(self, url):
        """Helper method to fetch meals from the given URL"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            meals = data.get('meals')
            if meals is None:
                print(f"No meals found for: {self.ingredient}")
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
        print(f"{self.ingredient.capitalize()} Meals Available:\n")
        for meal in meals:
            name = meal.get("strMeal", "Unknown Meal")
            image_url = meal.get("strMealThumb", "No Image Available")
            print(f"Meal Name: {name}")
            print(f"Image URL: {image_url}")
            print("-" * 40)