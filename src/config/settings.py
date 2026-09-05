import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Clé d'API
api_key = os.getenv("MAL_API_KEY")

# Nom d'utilisateur
user_name = os.getenv("MAL_USER_NAME")

NOMBRE_TENTATIVES_DEFAUT = 3
DELAI_TENTATIVE_DEFAUT = 5
MAL_API_URL = "https://api.myanimelist.net/v2/users/{user_name}/animelist"
MAL_API_FIELDS = "list_status"
