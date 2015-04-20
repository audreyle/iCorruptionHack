from flask import Flask
import json
from peewee import *

app = Flask(__name__)

with open('keys.json','r') as keysfile:
    keys = json.load(keysfile)
    postgres_keys = keys['postgres']
    name = postgres_keys['database']
    del postgres_keys['database']

db = PostgresqlDatabase(name, **postgres_keys)
