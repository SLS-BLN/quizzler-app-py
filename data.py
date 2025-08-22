import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("data.log"),
        logging.StreamHandler()
    ]
)

API_ENDPOINT = "https://opentdb.com/api.php"
parameters = {"amount": 10, "type": "boolean"}

def fetch_questions(url=API_ENDPOINT, params=None):
    if params is None:
        params = parameters
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        logging.info("Successfully fetched quiz data.")
        return response.json().get("results", [])
    except requests.RequestException as e:
        logging.error(f"Failed to fetch quiz data: {e}")
        return []
