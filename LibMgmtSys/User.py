import uuid


class User:
    def __init__(self, name: str, mobile_no: str):
        self.__ID: str = uuid.uuid4()
        self.name: str = name
        self.mobile_no: str = mobile_no
        
    def __str__(self):
        return f'User -> Name: {self.name}, MNo: {self.mobile_no}'