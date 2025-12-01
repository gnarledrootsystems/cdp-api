from quart import Blueprint

drugbp = Blueprint('drug', __name__)

@drugbp.route('/')
async def index():
    return 'Hello Drugs'

@drugbp.route('/import')
async def importer():
    return "Importing Drugs"