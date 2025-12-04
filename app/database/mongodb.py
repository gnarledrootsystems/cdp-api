import os
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure
from flask import Flask, current_app, g, has_app_context

mongodb = PyMongo()

def init_db(app):
    try:
        mongodb.init_app(app)
        mongodb.db.command('ping')
        print("MongoDB connection successful!")
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
def get_db():
    if mongodb.db is not None:
        return mongodb.db
    
    # Add error handling
    return None

def get_cx():
    if mongodb.cx is not None:
        return mongodb.cx
    
    return None