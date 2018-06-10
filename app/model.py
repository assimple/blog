from sqlalchemy.orm import Session

from blog.app.db import User


class TableUser(object):
    def __init__(self):
        self.ses = Session()

    def add_user(self, username, password):
        user = User(username=username, password=password)
        self.ses.add(user)
        self.ses.commit()

    def encrypt(self):
        return

    def check_user(self, username, password):
        elem1 = self.ses.query(User).filter(User.username == username).first()
        elem2 = self.ses.query(User).filter(User.password == password).first()
        print(elem1, elem2)
    def delete_user(self):
        pass
class TablePost(object):
    def __init__(self):
        self.ses = Session()
    def add_post(self,title,content):
        pass

if __name__ == "__main__":
    dp = TableUser()
    # dp.add_user('xiaoming', '123456')
    dp.check_user("xiao","123")