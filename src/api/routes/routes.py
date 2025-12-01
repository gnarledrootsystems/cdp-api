from . import bp
from quart import request

@bp.route("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}