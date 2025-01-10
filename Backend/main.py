from flask import Flask, Blueprint, request, jsonify
from secrets import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

main_blueprint = Blueprint('main', __name__)

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

def get_db_connection():
    try:
        connection = engine.connect()
        return connection
    except OperationalError as err:
        print(f"OperationalError: {err}")
        return None



app = Flask(__name__)
