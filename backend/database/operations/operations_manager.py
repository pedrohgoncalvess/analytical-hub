class OperationsManager:
    def __init__(self,
                 error: bool = False,
                 message: str | Exception = None,
                 status_code: int = None) -> None:
        self.error = error
        self.message = message
        self.status_code = status_code

        if error and message is None:
            self.message = "Error not mapped."
