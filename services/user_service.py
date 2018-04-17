from models.user import User


class UserService:

    users = {}

    @staticmethod
    def get_users():
        return UserService.users

    @staticmethod
    def add_user(username, displayName, department):
        user = User(username, displayName, department)
        UserService.users[user.username] = user
        return user.username, user.displayName, user.department

    @staticmethod
    def update_user(username, displayName, department):
        if username in UserService.users:
            user = UserService.users.get(username)
            user.displayName = displayName
            user.department = department
        return username

    @staticmethod
    def get_user(username):
        return UserService.users.get(username)

    @staticmethod
    def delete_user(username):
        if username in UserService.users:
            UserService.users.pop(username)
            return True
        else:
            return False