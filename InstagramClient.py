from instagrapi import Client


class InstagramClient:
    username = None
    password = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post_image(self, photo_path, comment):
        cl = Client()
        cl.login(self.username, self.password)
        cl.photo_upload(photo_path, comment)
        cl.logout()
