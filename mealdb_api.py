import requests

BASE_URL_SEARCH = "https://www.themealdb.com/api/json/v1/1/search.php"
BASE_URL_LOOKUP = "https://www.themealdb.com/api/json/v1/1/lookup.php"

def search_meal(query):
    params = {"s": query}
    response = requests.get(BASE_URL_SEARCH, params=params)
    if response.status_code == 200:
        return response.json().get("meals", [])
    else:
        print("Error:", response.text)
        return []

def get_meal_details(meal_id):
    params = {"i": meal_id}
    response = requests.get(BASE_URL_LOOKUP, params=params)
    if response.status_code == 200:
        meals = response.json().get("meals", [])
        return meals[0] if meals else None
    else:
        print("Error:", response.text)
        return None
