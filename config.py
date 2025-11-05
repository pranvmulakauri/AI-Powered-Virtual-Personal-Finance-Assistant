import os
from dotenv import load_dotenv

load_dotenv()

# Security Settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ENCRYPTION_ENABLED = True

# API Settings
BANK_API_TIMEOUT = 5
MAX_CONCURRENT_USERS = 5000

# Database Settings
DATABASE_PATH = "data/"

# Budget Settings
BUDGET_WARNING_THRESHOLD = 0.9  # Warn at 90% of budget

# NLP Settings
CHATBOT_CONFIDENCE_THRESHOLD = 0.7
