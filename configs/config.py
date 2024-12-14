from dotenv import dotenv_values

DB_URL = dotenv_values(".env")['DB_URL']
DB_NAME = dotenv_values(".env")['DB_NAME']
SESSION_SECRET = dotenv_values(".env")['SESSION_SECRET']
SESSION_ADMIN_SECRET = dotenv_values(".env")['SESSION_ADMIN_SECRET']
SESSION_EXPIRED_IN_MINUTES = 15
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "https://ner-frontend-client.vercel.app"]
MT_SERVER_ID = dotenv_values(".env")['MT_SERVER_ID']
DEBUG_MODE = True if dotenv_values(".env")['DEBUG_MODE'] == "true" else False
CLIENT_WEB_URL = 'https://ner-frontend-client.vercel.app'