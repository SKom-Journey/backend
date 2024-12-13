from dotenv import dotenv_values

DB_URL = dotenv_values(".env")['DB_URL']
DB_NAME = dotenv_values(".env")['DB_NAME']
SESSION_SECRET = dotenv_values(".env")['SESSION_SECRET']
SESSION_ADMIN_SECRET = dotenv_values(".env")['SESSION_ADMIN_SECRET']
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "https://ner-frontend-client.vercel.app"]