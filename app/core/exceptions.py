"""Domain Exceptions."""
class DocAnalyzerException(Exception):
    def __init__(self, message: str, code: str = "ERROR", status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code

class AuthenticationError(DocAnalyzerException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, "AUTH_ERROR", 401)

class DocumentNotFoundError(DocAnalyzerException):
    def __init__(self, message: str = "Document Not Found"):
        super().__init__(message, "NOT_FOUND", 404)

class ValidationError(DocAnalyzerException):
    def __init__(self, message: str = "Validation Failed"):
        super().__init__(message, "VALIDATION_FAILED", 400)
