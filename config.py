import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # General Flask app Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'idk'

    # Redis connection
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_DB = os.environ.get("REDIS_DB") or 0

    # Twilio API credentials
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
