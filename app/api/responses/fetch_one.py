class FetchOneOutput(object):
    def __init__(self, data, message="", success=False) -> None:
        self.data = data
        self.message = message
        self.success = success

    def response(self):
        return {
            "data": self.data,
            "message": self.message,
            "success": self.success,
        }
