import email
import imp
from multiprocessing.spawn import import_main_path


from user import User
from post import Post

appUserOne = User('email.com', 'zoz', "pwl", "student")
appUserOne.getUserInfo()

newPost = Post("hoo", appUserOne.name)
newPost.getPostInfo()
