import logging
logging.basicConfig(level=logging.INFO)

class SessionMemory:
    def __init__(self):
        self.history = []

    def add_history(self, sender, message):
        self.history.append({"sender": sender, "message": message})

    def get_history(self):
        return self.history
