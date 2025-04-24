import requests
from utils.config import app_config, env_config
from utils.logger import logger

base_url = app_config["api_url"]
app_api_key = env_config.APP_API_KEY

headers = {
    "accept": "application/json",
    "api-key": app_api_key
}


def get_llms():
    llm_options_endpoint = f"{base_url}/llm/llm_options"
    logger.info(f"Sending GET request to {llm_options_endpoint}")

    try:
        response = requests.get(url=llm_options_endpoint, headers=headers)
        response.raise_for_status()
        logger.info("Successfully fetched LLM options.")
        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch LLM options: {e}")
        return {"error": "Unable to fetch LLM options"}
