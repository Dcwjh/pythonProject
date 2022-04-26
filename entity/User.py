class User(object):
    def __init__(self, username, password, level): # 0代表普通用户， 1代表业务员，2代表审核员， 3代表管理员
        self.ID = ""
        self.username = username
        self.password = password
        self.level = level

    def __str__(self) -> str:
        return "ID: " + str(self.ID) + ", username : " + self.username + ",   password ： " + self.password + ",    level:" + str(self.level)