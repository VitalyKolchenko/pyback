from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/<name>")
async def test(request,name):
    return json({"hello22": name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)