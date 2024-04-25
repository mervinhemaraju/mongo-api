class Distinct(object):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        self.success = True

    def response(self):
        return {"message": self.message, "data": self.data, "success": self.success}
