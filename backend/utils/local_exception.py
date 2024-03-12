class LocalException:
    def __init__(self, error_message: str = "Unexpected error", status_code: int = 500, ) -> None:
        self.error_message = error_message
        self.status_code = status_code
