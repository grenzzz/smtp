class Error(Exception):
    pass

class TransientError(Error):
    pass

class PermanentError(Error):
    pass

class ProtectedError(Error):
    pass
