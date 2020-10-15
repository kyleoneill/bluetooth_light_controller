from dotenv import load_dotenv
import os
import controller
from flask import Flask, request
import time
load_dotenv()

app = Flask(__name__)
strip_controller = controller.Controller(os.getenv("MAC_ADDRESS"))


def validate_colors(red, green, blue):
    try:
        red = int(red)
        green = int(green)
        blue = int(blue)
        return True, red, green, blue
    except ValueError:
        return False, 0, 0, 0


@app.route("/set_color", methods=["POST"])
def set_color():
    print("Got here")
    red = request.args.get("red")
    green = request.args.get("green")
    blue = request.args.get("blue")
    (request_valid, red, green, blue) = validate_colors(red, green, blue)
    if not request_valid:
        return "Bad request"
    try:
        strip_controller.change_color((red, green, blue))
        return "Color changed"
    except AssertionError:
        return "Invalid color range"


if __name__ == "__main__":
    port = os.getenv("PORT")
    host = os.getenv("HOST")
    app.run(host=host, port=port)
