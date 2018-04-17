from uuid import uuid1


class User:
    def __init__(self, username, displayName, department):
        self.username = username
        self.displayName = displayName
        self.department = department
