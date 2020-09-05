from flask import Flask, redirect
import os.path
import uvicorn
from json import load
json_load = load


app = Flask(__name__)

redirect_list = json_load(
    open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "redirect_list.json"
    ))
)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path in redirect_list:
        return redirect(redirect_list[path], 301)
    else:
        return f"/{path} not found."


if __name__ == '__main__':
    uvicorn.run(app, port=11452)
