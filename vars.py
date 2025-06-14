#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28712726"))
API_HASH = environ.get("API_HASH", "06acfd441f9c3402ccdb1945e8e2a93b")
BOT_TOKEN = environ.get("BOT_TOKEN", "7894993684:AAGossQUEP_OknJfPQvAJLPUHOrUemFxX1g")
OWNER = int(environ.get("OWNER", "1003575883"))
CREDIT = "CHITIJRAJPUT"
AUTH_USER = os.environ.get('AUTH_USERS', '1003575883').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
