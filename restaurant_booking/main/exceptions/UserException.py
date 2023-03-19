class UserException(Exception):

    def __init__(self, message, status=400):
        self.status = status
        self.message = message
        super().__init__(self.message)