class FetchAllOutput(object):
    def __init__(
        self, data, page, total_pages, total_documents, message="", success=False
    ) -> None:
        self.data = data
        self.message = message
        self.page = page
        self.total_pages = total_pages
        self.total_documents = total_documents
        self.success = success

    def response(self):
        return {
            "data": self.data,
            "message": self.message,
            "page": self.page,
            "total_pages": self.total_pages,
            "total_documents": self.total_documents,
            "success": self.success,
        }
