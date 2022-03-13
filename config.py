import os

# DEBUG = False
# CORS_HEADERS = 'Content-Type'
SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpYSY78&huqlCOGI4nss'
SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = './flask_session'
SESSION_FILE_THRESHOLD = 10 
MONGODB_HOST = f"mongodb+srv://{os.environ['USER']}:{os.environ['PASSWORD']}@cluster0.x4s44.mongodb.net/{os.environ['DB']}?retryWrites=true&w=majority"