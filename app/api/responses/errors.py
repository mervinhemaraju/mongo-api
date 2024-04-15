from flask_restful import fields


class ErrorGeneral(object):
    error_fields = {
        "message": fields.String,
        "success": fields.Boolean,
    }

    def __init__(self, message):
        self.message = message
        self.success = False


class ErrorOps(object):
    def __init__(self, message):
        self.message = message
        self.success = False

    def response(self):
        return {"message": self.message, "success": self.message}
