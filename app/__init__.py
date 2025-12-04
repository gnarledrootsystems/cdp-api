import os

from flask import Flask
#from instance.config import DevelopmentConfig, ProductionConfig
from dotenv import load_dotenv
from app.database.mongodb import init_db
from app.modules.importer import importer

def create_app(test_config=None):
    load_dotenv()
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    print("Printing App.Config")
    print(app.config)
    
    #app.config.from_pyfile('config.py')
    
    app.config["ENV"] = "development"
    
    if app.config['ENV'] == 'development':
        print("Loading Dev Config")
        #app.config.from_object(DevelopmentConfig)
        app.config.from_object('config.DevelopmentConfig')
    elif app.config['ENV'] == 'production':
        print("Loading Prod Config")
        #app.config.from_object(ProductionConfig)
    
    #app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    print(f"MONGO_URI: {app.config["MONGO_URI"]}")

    init_db(app)
    app = importer(app)

    #with app.app_context():
        
    print(app.instance_path)    
    
    


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        
        return 'Hello, World!'

    return app