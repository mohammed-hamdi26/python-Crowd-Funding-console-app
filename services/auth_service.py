from utils.file_handler import load_data, save_data


class AuthService:
    def __init__(self):
        self.users = load_data("json/users.json")
        self.current_user = None

    def register(self, user):
        for u in self.users:
            if u["email"] == user.email:
                return False

        self.users.append(user.to_dict())
        self.current_user = user.to_dict()
        save_data("json/users.json", self.users)
        print("User registered successfully ✅")

        return True

    def login(self, email, password):
        for u in self.users:
            if u["email"] == email and u["password"] == password:
                self.current_user = u
                return True
        return False

    def logout(self):
        self.current_user = None

    def get_last_user_id(self):
        return self.users[-1]["id"]
