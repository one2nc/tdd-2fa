from flask import Flask, request
import server.logic as logic
app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    device_id = request.get_json().get("device_id")
    secret = logic.register_device(device_id)[str(device_id)].secret
    return {
        "registered": True,
        "secret": secret
    }


@app.route("/is_registered/<device_id>", methods=["GET"])
def is_registered(device_id):
    if logic.get_device_info(device_id):
        return {"is_registered": True}

    return {"is_registered": False}


@app.route("/validate/<device_id>", methods=["GET"])
def validate_otp(device_id):
    received_otp = request.get_json().get("OTP")
    if logic.validate_otp(device_id=device_id, received_otp=received_otp):
        return {"is_valid": True}

    return {"is_valid": False}


if __name__ == '__main__':
    app.run()



