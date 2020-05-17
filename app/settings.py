from dotenv import load_dotenv
import os


def init():
    cur_dir = os.path.dirname(__file__)
    load_dotenv(os.path.join(cur_dir, '.env'))
