from quart import Quart
from app import create_app

app = create_app('Development')

def run() -> None:
    app.run()