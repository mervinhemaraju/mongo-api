from flask_restful import fields


class WriteOps(object):
    wo_fields = {
        "message": fields.String,
        "count": fields.Integer,
        "success": fields.Boolean,
    }

    def __init__(self, message, count):
        self.message = message
        self.count = count
        self.success = True
