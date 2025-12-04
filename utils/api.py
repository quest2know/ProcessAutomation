import requests # for making API requests
import datetime     # for timestamping files
import time 
def fetch_data_from_api(url,logger,retries = 3,delay = 2):
    """Fetch data from the given API endpoint with retry mechanism."""
    attempt = 0
    while attempt < retries:
        try:
            logger.info(f"Fetching data from API: {url}, Attempt: {attempt + 1}")
            response = requests.get(url)
            logger.info(f"Received response with status code: {response.status_code}")
            logger
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return parsed JSON data
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            logger.error(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)
    raise Exception(f"Failed to fetch data from API after {retries} attempts.")
