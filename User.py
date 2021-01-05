class User:
    def __init__(self, username, password):
        self.__username=username
        self.__password=password

    def getUsername(self):
        return self.__username

    def setUsername(self,username):
        self.__username=username

    def getPassword(self):
        return self.__password

    def setPassword(self,password):
        self.__password=password

class Manager(User):
    def __init__(self, username, password, nama):
        super().__init__(username, password)
        self.__nama=nama

    def getNama(self):
        return self.__nama
        