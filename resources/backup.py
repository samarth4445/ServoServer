from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import control


# docker build -t gocycle-server .
# docker run -dp 5005:5000 -w /app -v "/e/server_cycle:/app" gocycle-server

blp = Blueprint("control", __name__, description="OTP generation.")

@blp.route("/control")
class OtpGenerator(MethodView):
    def post(self):
        request_data = request.get_json()
        control["servoAddress"] = request_data["servoAddress"]
        return {"message": "Control signal sent."}

@blp.route("/control-stop")
class ServoStop(MethodView):
    def get(self):
        control["servoAddress"] = "0"
        return {"message": "Stopped."}
    
    def post(self):
        request_data = request.get_json()
        servoAddress = list(request_data.keys())[0]
        direction = request_data[list(request_data.keys())[0]]

        return {"message": "Stopped."}

@blp.route("/control-get")
class OtpGet(MethodView):
    def get(self):
        return control

