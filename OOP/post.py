class Post:
    def __init__(self, message, author) -> None:
        self.message = message
        self.author = author

    def getPostInfo(self):
        print(f"Post: {self.message} written by {self.author}")
