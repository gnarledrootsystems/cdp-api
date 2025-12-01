from quart import Quart
from src.api.blueprints.drug import drugbp

app = Quart(__name__)

app.register_blueprint(drugbp, url_prefix="/drug")

def run() -> None:
    app.run()