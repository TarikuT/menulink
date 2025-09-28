import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_TITLE = os.getenv("API_TITLE", "MenuLink API")
API_DEBUG = os.getenv("API_DEBUG", "false").lower() == "true"

# Default: connect to Postgres service from docker-compose
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://menulink:menulink@db:5432/menulink"
)
