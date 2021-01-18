class UserNotExistsException(Exception):
    def __init__(self,msg):
        self.__msg = msg
