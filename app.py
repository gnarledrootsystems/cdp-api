from quart import Quart
from quart_schema import QuartSchema

from src.modules.importer import importer

from src.api.blueprints.drug import drugbp

def create_app(mode='Development'):
    app = Quart(__name__)
    
    QuartSchema(app)
    
    # CLI Commands
    app = importer(app)
    
    # Blueprints
    app.register_blueprint(drugbp, url_prefix="/drug")
    
    @app.route('/')
    async def hello():
        return 'Hello CDP API.'
    
    return app