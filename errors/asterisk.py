

class AsteriskError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)

    
    def __str__(self):
        return f"Error code:{self.code}, Reasone:{self.message}"
    
    def __repr__(self):
        return f"{self.code}: {self.message}"
