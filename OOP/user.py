import email


class User:
    def __init__(self, email, name, password, jobTitle):
        self.email = email
        self.name = name
        self.password = password
        self.jobTitle = jobTitle

    def changePassword(self, newPassword):
        self.password = newPassword

    def changeJobTitle(self, newJobTitle):
        self.jobTitle = newJobTitle

    def getUserInfo(self):
        print(
            f"User {self.name} currently work as a {self.jobTitle} and you can contact them at {self.email} "
        )


